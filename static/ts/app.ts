const input = document.getElementById('user_input') as HTMLInputElement;
const button = document.getElementById('button') as HTMLButtonElement;
const output = document.getElementById('output') as HTMLElement;

// add event listener
button.addEventListener('click', async () => {
  const userMessage = input.value;

  // send to backend
  const res = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: userMessage })
  });

  // show backend response
  const data: { reply: string } = await res.json();
  output.textContent = data.reply;
});
