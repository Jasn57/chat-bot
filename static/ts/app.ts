const input = document.getElementById('user_input');
const button = document.getElementById('button');
const output = document.getElementById('output');

// when button is clicked set user input to user input
button.addEventListener('click', async () => {
const userMessage = input.value;

// send to backend
const res = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: userMessage })
});

// show backend response
const data = await res.json();
output.textContent = data.reply;
});
