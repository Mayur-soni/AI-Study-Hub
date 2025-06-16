function showTab(tabName) {
  document.querySelectorAll('.code-tab').forEach(tab => {
    tab.classList.remove('active');
  });
  document.getElementById(tabName).classList.add('active');
}

function runCode() {
  const html = document.getElementById('html').value;
const css = document.getElementById('css').value;
const js = document.getElementById('js').value;

window.open("/coding/blank/?html=" + encodeURIComponent(html) + "&css=" + encodeURIComponent(css) + "&js=" + encodeURIComponent(js));
}