var params = {
  container: document.querySelector("#lottie3"),
  renderer: "canvas",
  loop: true,
  autoplay: true,
  path: "data/graph.json",
};

var anim;

anim = lottie.loadAnimation(params);
