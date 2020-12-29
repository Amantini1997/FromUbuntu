const d3 = window.d3

function updateDelay(slider) {
    window.delay = +slider.value
}

var dataArray

function generateGraph() {
    dataArray = window.dataInput
    const d3Node = document.querySelector('svg')
    d3Node.innerHTML = "" 
    for (var i = 0; i < dataArray.length; i++)
       d3Node.innerHTML += `<text class="rects" id="rect${dataArray[i]}" x="${i*10}" y="10" >${dataArray[i]}</text>`
}

function animateGraph() {
    bubbleSort()
}

function generateAndAnimateGraph() {
    generateGraph()
    animateGraph()
}

async function bubbleSort() {
    let dataLength = dataArray.length
    let swapped
    do {
        swapped = false
        for (let i = 0; i < dataLength; i++) {
            if (dataArray[i] > dataArray[i + 1]) {

                let temp = dataArray[i]
                dataArray[i] = dataArray[i + 1]
                dataArray[i + 1] = temp
                swapped = true
                // call function here for swap animation...
                await swapAnimation(dataArray[i], i, dataArray[i + 1], i + 1); // did not work
            }
        }
    } while (swapped)
    return console.log(dataArray)
}

function swapAnimation(d, i, d1, i1) {
    const durationTime = window.delay
    var sel = `#rect${d}`, sel1 = `#rect${d1}`
    var x1 = d3.select(sel1).attr("x")
    var x  = d3.select(sel).attr("x")
    return Promise.all([
        d3.select(sel)
          .transition()
          .duration(durationTime)
          .attr("x", x1)
          .end(),

        d3.select(sel1)
          .transition()
          .duration(durationTime)
          .attr("x", x)
          .end()
    ])
}