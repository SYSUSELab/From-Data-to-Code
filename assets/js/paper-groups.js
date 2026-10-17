(function () {
  "use strict";

  function findTarget(hash) {
    if (!hash) return null;
    try {
      return document.getElementById(decodeURIComponent(hash.slice(1)));
    } catch (error) {
      return null;
    }
  }

  function revealTarget() {
    var target = findTarget(window.location.hash);
    var group = target && target.closest(".paper-category");
    if (!group) return;
    group.open = true;
    window.requestAnimationFrame(function () {
      target.scrollIntoView({ block: "start" });
      var focusTarget = target === group ? group.querySelector("summary") : target;
      if (target !== group && !focusTarget.hasAttribute("tabindex")) focusTarget.tabIndex = -1;
      focusTarget.focus({ preventScroll: true });
    });
  }

  // Expand before native anchor navigation, including a repeated click on the same hash.
  document.addEventListener("click", function (event) {
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    var link = event.target.closest("a[href]");
    if (!link || link.target === "_blank") return;
    var url = new URL(link.href, window.location.href);
    if (url.origin !== window.location.origin || url.pathname !== window.location.pathname) return;
    var target = findTarget(url.hash);
    var group = target && target.closest(".paper-category");
    if (!group) return;
    group.open = true;
    if (url.hash === window.location.hash) revealTarget();
  });

  window.addEventListener("hashchange", revealTarget);
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", revealTarget, { once: true });
  } else {
    revealTarget();
  }
})();
