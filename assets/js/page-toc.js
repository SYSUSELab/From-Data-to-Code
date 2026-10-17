(function () {
  "use strict";

  function initialize() {
    var main = document.querySelector(".main-content > main");
    if (!main || main.querySelector(".reading-layout")) return;

    var headings = Array.from(main.querySelectorAll("h2, h3")).filter(function (heading) {
      return !heading.closest(".site-hero, .paper-card, .no_toc, [data-toc-exclude]");
    });
    if (headings.length < 2) return;

    var layout = document.createElement("div");
    layout.className = "reading-layout";
    var content = document.createElement("div");
    content.className = "reading-content";
    while (main.firstChild) content.appendChild(main.firstChild);
    layout.appendChild(content);
    main.appendChild(layout);

    var nav = document.createElement("nav");
    nav.className = "page-toc";
    nav.setAttribute("aria-label", "On this page");
    var panel = document.createElement("details");
    panel.className = "page-toc__panel";
    var summary = document.createElement("summary");
    summary.className = "page-toc__summary";
    var label = document.createElement("span");
    label.className = "page-toc__title";
    label.textContent = "On this page";
    var count = document.createElement("span");
    count.className = "page-toc__count";
    var sectionCount = headings.filter(function (heading) { return heading.tagName === "H2"; }).length;
    count.textContent = (sectionCount || headings.length) + " sections";
    var currentLabel = document.createElement("span");
    currentLabel.className = "page-toc__current";
    var toggleIcon = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    toggleIcon.setAttribute("class", "page-toc__toggle-icon");
    toggleIcon.setAttribute("viewBox", "0 0 24 24");
    toggleIcon.setAttribute("fill", "none");
    toggleIcon.setAttribute("stroke", "currentColor");
    toggleIcon.setAttribute("stroke-width", "1.8");
    toggleIcon.setAttribute("aria-hidden", "true");
    toggleIcon.innerHTML = '<path d="M9 6h11M9 12h11M9 18h11"/><circle cx="4" cy="6" r="1"/><circle cx="4" cy="12" r="1"/><circle cx="4" cy="18" r="1"/>';
    summary.append(toggleIcon, label, count, currentLabel);
    panel.appendChild(summary);
    nav.appendChild(panel);

    var list = document.createElement("ol");
    list.className = "page-toc__list";
    panel.appendChild(list);
    var links = [];
    var section = 0;
    var parentItem = null;

    headings.forEach(function (heading, index) {
      var copy = heading.cloneNode(true);
      copy.querySelectorAll(".anchor-heading, .rq-icon, [aria-hidden='true']").forEach(function (node) {
        node.remove();
      });
      var title = copy.textContent.replace(/\s+/g, " ").trim();
      if (!heading.id) {
        var base = title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "section";
        var id = base;
        var suffix = 2;
        while (document.getElementById(id)) id = base + "-" + suffix++;
        heading.id = id;
      }
      if (!heading.hasAttribute("tabindex")) heading.tabIndex = -1;

      var item = document.createElement("li");
      var link = document.createElement("a");
      link.className = "page-toc__link";
      link.href = "#" + encodeURIComponent(heading.id);
      var number = document.createElement("span");
      number.className = "page-toc__number";
      number.setAttribute("aria-hidden", "true");
      var text = document.createElement("span");
      text.className = "page-toc__text";
      text.textContent = title;

      if (heading.tagName === "H2" || !parentItem) {
        section += 1;
        number.textContent = String(section).padStart(2, "0");
        list.appendChild(item);
        parentItem = item;
      } else {
        var sublist = parentItem.querySelector("ol");
        if (!sublist) {
          sublist = document.createElement("ol");
          sublist.className = "page-toc__sublist";
          parentItem.appendChild(sublist);
        }
        number.textContent = "\u00b7";
        sublist.appendChild(item);
      }
      link.append(number, text);
      item.insertBefore(link, item.firstChild);
      links[index] = link;
    });

    // Keep the navigation outside the article and all of its containing blocks.
    document.body.appendChild(nav);
    nav.style.position = "fixed";
    nav.style.margin = "0";
    nav.style.zIndex = "90";
    var wide = window.matchMedia("(min-width: 80rem)");
    var drawerOpen = false;
    var header = document.getElementById("main-header");
    var siteHeader = document.querySelector(".side-bar .site-header");
    var desktopMenu = window.matchMedia("(min-width: 50rem)");
    var activeIndex = -1;
    var scheduled = false;
    var anchorOffset = 0;

    function positionNavigation() {
      var rem = parseFloat(getComputedStyle(document.documentElement).fontSize) || 16;
      var headerHeight = header ? header.getBoundingClientRect().height : 0;
      if (!desktopMenu.matches && siteHeader) {
        headerHeight = Math.max(headerHeight, siteHeader.getBoundingClientRect().height);
      }
      document.documentElement.style.setProperty("--reading-header-height", headerHeight + "px");
      var box = layout.getBoundingClientRect();
      var viewportWidth = document.documentElement.clientWidth;
      var edge = desktopMenu.matches ? 16 : 12;
      var width = wide.matches ? 13 * rem : (panel.open ? 19 * rem : 44);
      width = Math.min(width, viewportWidth - 2 * edge);
      nav.style.left = "auto";
      nav.style.right = edge + "px";
      var top = headerHeight + 1.5 * rem;
      nav.style.top = top + "px";
      nav.style.width = width + "px";

      // Reserve a right-hand column; opening the compact drawer overlays that column.
      var reservedWidth = wide.matches ? width : 44;
      var gap = (wide.matches ? 1.5 : 0.75) * rem;
      var contentRight = viewportWidth - edge - reservedWidth - gap;
      layout.style.paddingRight = Math.max(0, box.right - contentRight) + "px";
      layout.style.paddingTop = "0";
      anchorOffset = headerHeight + 1.5 * rem;
      document.documentElement.style.setProperty("--reading-anchor-offset", anchorOffset + "px");
    }

    function updateActive() {
      scheduled = false;
      var boundary = anchorOffset + 4;
      var current = 0;
      headings.forEach(function (heading, index) {
        if (heading.getBoundingClientRect().top <= boundary) current = index;
      });
      if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2) {
        current = headings.length - 1;
      }
      if (current === activeIndex) return;
      if (activeIndex >= 0) links[activeIndex].removeAttribute("aria-current");
      links[current].setAttribute("aria-current", "location");
      currentLabel.textContent = links[current].querySelector(".page-toc__text").textContent;
      activeIndex = current;
    }

    function scheduleUpdate() {
      if (scheduled) return;
      scheduled = true;
      window.requestAnimationFrame(updateActive);
    }

    function placeNavigation() {
      nav.classList.toggle("page-toc--rail", wide.matches);
      if (wide.matches) {
        panel.open = true;
        summary.tabIndex = -1;
      } else {
        panel.open = drawerOpen;
        summary.removeAttribute("tabindex");
      }
      updateToggleLabel();
      positionNavigation();
      scheduleUpdate();
    }

    summary.addEventListener("click", function (event) {
      if (wide.matches) event.preventDefault();
    });
    function updateToggleLabel() {
      if (wide.matches) {
        summary.removeAttribute("aria-label");
        summary.removeAttribute("title");
      } else {
        var action = panel.open ? "Close page contents" : "Open page contents";
        summary.setAttribute("aria-label", action);
        summary.title = action;
      }
    }
    panel.addEventListener("toggle", function () {
      if (!wide.matches) drawerOpen = panel.open;
      updateToggleLabel();
      positionNavigation();
      scheduleUpdate();
    });
    nav.addEventListener("click", function (event) {
      if (event.target.closest(".page-toc__link") && !wide.matches) {
        drawerOpen = false;
        panel.open = false;
        // Update the anchor clearance before the browser follows the link.
        positionNavigation();
      }
    });
    nav.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && !wide.matches && panel.open) {
        panel.open = false;
        drawerOpen = false;
        updateToggleLabel();
        positionNavigation();
        summary.focus();
      }
    });
    wide.addEventListener("change", placeNavigation);
    window.addEventListener("scroll", scheduleUpdate, { passive: true });
    window.addEventListener("resize", function () {
      positionNavigation();
      scheduleUpdate();
    });
    window.addEventListener("hashchange", scheduleUpdate);
    if (window.ResizeObserver) {
      var observer = new ResizeObserver(function () {
        positionNavigation();
        scheduleUpdate();
      });
      observer.observe(content);
      observer.observe(nav);
      if (header) observer.observe(header);
      if (siteHeader) observer.observe(siteHeader);
    }
    placeNavigation();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize, { once: true });
  } else {
    initialize();
  }
})();
