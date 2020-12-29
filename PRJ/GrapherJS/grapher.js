const BLANK_SPACE = "&nbsp;"

window.addEventListener("DOMContentLoaded", init, false)

function init() {
    window.lineCounter = 0
    window.delay = 1000
    window.dataInput = [9, 1, 5, 7, 2, 4, 3] // TODO make this dynamic
    addExampleCode()
}

function addExampleCode() {
    const lines = [
        'function example() {',
        '&emsp;console.log("Hello, World!");',
        '}'
    ]
    lines.forEach(addCodeCommentLine)
    generateCode()
}

function generateCode() {
    const rawLines = getRawLines()
    const codeContainer = document.getElementById("code-highlighter")
    codeContainer.innerHTML = ""
    rawLines.forEach((line, index) => {
        const codeNode = line.querySelector(".line-code")
        const code = (codeNode.innerHTML === codeNode.dataset.placeholder) ? "" : codeNode.innerHTML
        const commentNode = line.querySelector(".line-comment")
        const comment = (commentNode.innerHTML === commentNode.dataset.placeholder) ? "" : commentNode.innerHTML
        if (code) {
            const codeLine = document.createElement("div")
            codeLine.classList.add(`code-line-${index}`)
            codeLine.innerHTML = code
            codeLine.dataset.comment = comment
            codeContainer.appendChild(codeLine)  
        }              
    })
    // const formattedLines = lines.map((line, index) => `<div class="line-${index}">${line}</div>`)
    // document.getElementById("code").innerHTML = formattedLines.join("")
}

function sanitise(code) {
    return code.replaceAll("<", "&lt;").replaceAll(">", "&gt;")
}

function parseEscapeChars(event) {
    const ENTER_CODE = 13
    event = event || window.event;
    const charCode = event.keyCode || event.which;
    if (charCode == ENTER_CODE) {
        event.preventDefault()
        addCodeCommentLine()
    }
    // const charStr = String.fromCharCode(charCode);
}

function addCodeCommentLine(text="") {
    const line = document.querySelector("template#line-template").content.cloneNode(true);
    line.querySelector(".counter").innerHTML = BLANK_SPACE + window.lineCounter++ +BLANK_SPACE
    const list = document.getElementById("lines-table__body")
    let codeCommentContainersList = Array.from(line.querySelector(".code-comment-ctn").children)
    
    // delete the content of code and comment on focus and re-add it
    // if the content has not been edited
    codeCommentContainersList.forEach(section => {
        const placeholder = section.getAttribute("data-placeholder")

        section.innerHTML = placeholder

        section.addEventListener("focus", event => {
            const value = event.target.innerHTML
            if (value === placeholder) event.target.innerHTML = ""
        })

        section.addEventListener("blur", event => {
            const value = event.target.innerHTML
            if (value === "") event.target.innerHTML = placeholder
        })
    })
    list.appendChild(line)
    const codeBlock = codeCommentContainersList[0]
    codeBlock.innerHTML = text
    codeBlock.focus()
}

function deleteLineFromDeleteButton(lineDeleteButton) {
    const line = lineDeleteButton.parentNode
    const deletedCounter = +line.querySelector(".counter").innerHTML.replaceAll(BLANK_SPACE, "") 
    window.lineCounter--
    let list = document.getElementById("lines-table__body")
    list.removeChild(line)

    const lines = getRawLines()
    lines.forEach(line => {
        const currentCounterNode = line.querySelector(".counter") 
        const currentCounter = +currentCounterNode.innerHTML.replaceAll(BLANK_SPACE, "") 
        if (currentCounter > deletedCounter) {
            currentCounterNode.innerHTML = BLANK_SPACE + currentCounter - 1 + BLANK_SPACE
        }
    })
}

// Return the raw lines without the template one
function getRawLines() {
    const listBody = document.querySelector("#lines-table__body")
    let rawLines = Array.from([...listBody.children])
    // remove template line
    rawLines.shift()
    return rawLines
}