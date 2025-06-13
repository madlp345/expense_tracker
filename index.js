const express = require('express');
const { spawn } = require('child_process');
const app = express();
const path = require('path');

const PORT = process.env.PORT || 5000;

// Serve static HTML file with terminal emulator (optional)
app.use(express.static('public'));
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html')); // if you have one
});

app.listen(PORT, () => {
  console.log(`App running on http://localhost:${PORT}`);

  const pythonProcess = spawn('python3', ['run.py'], {
    stdio: 'inherit',
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python script exited with code ${code}`);
  });
});
