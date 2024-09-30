import { streamGemini } from './gemini-api.js';

let form = document.querySelector('form');
let promptInput = document.querySelector('input[name="prompt"]');
let output = document.querySelector('.output');

form.onsubmit = async (ev) => {
  ev.preventDefault();
  output.textContent = 'Generating...';

  try {
    // Assemble the prompt.
    let contents = [
      {
        type: "text",
        text: promptInput.value,
      }
    ];

    // Call the multimodal model, and get a stream of results.
    let stream = streamGemini({
      model: 'gemini-1.5-flash',
      contents,
    });

    // Read from the stream and interpret the output as markdown.
    let buffer = [];
    let md = new markdownit();
    for await (let chunk of stream) {
      buffer.push(chunk);
      output.innerHTML = md.render(buffer.join(''));
    }
  } catch (e) {
    output.innerHTML += '<hr>' + e;
  }
};
