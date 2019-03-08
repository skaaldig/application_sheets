let stepcount = 0;


const bar = new ProgressBar.Line(container, {
    strokeWidth: 3,
    easing: 'easeOut',
    duration: 500,
    color: '#42f4a1',
    trailColor: '#eee',
    trailWidth: 1,
    svgStyle: {
        width: '100%',
        height: '100%'
    },
    text: {
        style: {
            // Text color.
            // Default: same as stroke color (options.color)
            color: '#ffffff',
            position: 'absolute',
            right: '0',
            top: '30px',
            padding: 0,
            margin: 0,
            transform: null
        },
        autoStyleContainer: false
    },
    from: { color: '#FFEA82' },
    to: { color: '#ED6A5A' }
});

const getSteps = function () {
    const text = document.getElementById("counter").innerHTML
    const numbers = text.match(/\d+/g)
    return [parseInt(numbers[0]), parseInt(numbers[1])]
}

const getCurrentStep = function () {
    const pageNums = getSteps();
    const interval = parseFloat(((100 / pageNums[1]) / 100).toFixed(5))
    return parseFloat((pageNums[0] * interval).toFixed(5))
}

bar.animate(getCurrentStep());