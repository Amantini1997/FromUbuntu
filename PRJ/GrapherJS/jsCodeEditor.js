const JS_CODE_EDITOR = "#js-code-editor"

require.config({ paths: 
                    { "vs": "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs" }
                })
window.MonacoEnvironment = { getWorkerUrl: () => proxy }
let proxy = URL.createObjectURL(new Blob([`
    self.MonacoEnvironment = {
        baseUrl: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min"
    };
    importScripts("https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs/base/worker/workerMain.min.js");
`], { type: "text/javascript" }))
require(["vs/editor/editor.main"], () => {
    window.jsCodeEditor = monaco.editor.create(document.querySelector(JS_CODE_EDITOR), {
        value: `/** 
*  Use this space to write the logic of the program, i.e. the javascript function 
*  that operates the algorithm. Use the "yield" keyword to tell the program 
*  which line to highlight at each stage.
* e.g.
*      yield 0 
*  This will highlight the 0th line (remember the program uses the array notation,
*  so the first element is the element at position 0)
* 
*  It is possible to return dynamic comments, for example if a the comment
*  depends on the value of a variable. In such case use the keyword yield to return
*  a JSON object of the form:
*  yield {
*      line: 0,
*      comment: "checking if element " + x + " >= " + y
*  }
* 
*  Write only the body of the function, do NOT include the function head
*  Avoid using comments and code on the same line as this would create a parsing issue
*  eg.
*     ==== GOOD ====
*      //increment counter
*      i = i + 1
*     
*     ==== BAD ====
*      i = i + 1 //increment counter
*/ 


// highlight the function call
yield 0

const LINE_DYNAMIC_COMMENT = "console.log()";
// highlight the console.log()
yield {
    line: 1, 
    comment: "printing " + LINE_DYNAMIC_COMMENT
} 
console.log("Hello, World!");

// highlight the end of the function
yield 2`,
        language: "javascript",
        theme: "vs-dark"
    })
})

function getJsCode() {
    const jsCommentedCode = window.jsCodeEditor.getValue()
    const jsUncommentedCode = removeCommentLines(jsCommentedCode)
    const jsCode = jsUncommentedCode.join("\n")
    return jsCode
}

function removeCommentLines(code) {
    // remove comments from code
    const SINGLE_LINE_COMMENT = "//"
    const MULTIPLE_LINE_COMMENT_OPEN = "/*"
    const MULTIPLE_LINE_COMMENT_CLOSE = "*/"
    let isMultipleLineComment = false
    let uncommentedCode = []
    const lines = code.split("\n")
    for(let line of lines) {
        const trimmedLine = line.trim()
        // line is the start of a multiple line comment
        if (trimmedLine.startsWith(MULTIPLE_LINE_COMMENT_OPEN)) isMultipleLineComment = true
        // line is a comment
        if (isMultipleLineComment || trimmedLine.startsWith(SINGLE_LINE_COMMENT)) {
            // line is the end of a multiple line comment
            if (trimmedLine.endsWith(MULTIPLE_LINE_COMMENT_CLOSE)) isMultipleLineComment = false
            continue
        }
        // remove empty lines
        if (trimmedLine === "") continue
        uncommentedCode.push(line)
    }
    return uncommentedCode
}

function generateJsFunctionFromCodeEditor() {
    var GeneratorFunction = Object.getPrototypeOf(function*(){}).constructor
    const jsCode = getJsCode()
    return new GeneratorFunction(jsCode)()
}

function hiLine(line) {
    const lineNumber = line.line ?? line
    const HIGHLIGHT = "highlight"
    if (document.currentLine) {
        document.currentLine.classList.remove(HIGHLIGHT)
    }
    const currentLine = document.querySelector(`.code-line-${lineNumber}`)
    currentLine.classList.add(HIGHLIGHT)
    document.currentLine = currentLine

    const comment = line.comment || currentLine.dataset.comment
    if (comment) {
        console.log(comment)
    }
}


function runHighlighter() {
    var iter = generateJsFunctionFromCodeEditor()
    var line = iter.next()
    var firstIteration = true
    var delay = window.delay
    const linesHighlighter = setInterval(() => {
        if (line.done) {
            clearInterval(linesHighlighter)
        } else if(!window.pause) {
            hiLine(line.value)
            line = iter.next()
            delay = window.delay
        } else {
            // execution is pause, check for awakes
            delay = 100
        }
    }, this.firstIteration 
        ? (firstIteration=false) & 0 
        : delay
    )
}