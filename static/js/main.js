const currentPath = window.location.pathname;

document.querySelectorAll(".nav-links a").forEach((link) => {
  if (link.getAttribute("href") === currentPath) {
    link.setAttribute("aria-current", "page");
  }
});

document.querySelectorAll("input[type='number']").forEach((input) => {
  input.addEventListener("input", () => {
    input.classList.toggle("has-value", input.value.trim().length > 0);
  });
});
