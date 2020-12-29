function play() {
    runHighlighter() // from grapher.js
    generateAndAnimateGraph() // from plotter.js
    window.pause = false
}

function pause() {
    window.pause = true
}