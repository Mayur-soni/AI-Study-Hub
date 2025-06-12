<script>
  let pyodideReady = false;
  let pyodide;

  async function loadPyodideAndPackages() {
    pyodide = await loadPyodide();
    pyodideReady = true;
  }

  loadPyodideAndPackages();

  function showTab(lang) {
    document.querySelectorAll('.code-tab').forEach(tab => tab.classList.remove('active'));
    document.getElementById(lang).classList.add('active');
  }

  async function runCode() {
    const html = document.getElementById('html').value;
    const css = "<style>" + document.getElementById('css').value + "</style>";
    const js = "<script>" + document.getElementById('js').value + "<\/script>";
    const python = document.getElementById('python').value;

    if (document.getElementById('python').classList.contains('active')) {
      document.getElementById('output').style.display = 'none';
      document.getElementById('python-output').style.display = 'block';
      document.getElementById('python-output').textContent = "Running Python...";
      if (pyodideReady) {
        try {
          let result = await pyodide.runPythonAsync(python);
          document.getElementById('python-output').textContent = result ?? 'Python code executed.';
        } catch (err) {
          document.getElementById('python-output').textContent = err;
        }
      } else {
        document.getElementById('python-output').textContent = "Python is still loading...";
      }
    } else {
      const output = document.getElementById('output');
      document.getElementById('python-output').style.display = 'none';
      output.style.display = 'block';
      output.srcdoc = css + html + js;
    }
  }
</script>

      aiSendButton.addEventListener('click', sendMessage);
      aiUserInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
          sendMessage();
        }
      });

      aiUserInput.focus();
    });
