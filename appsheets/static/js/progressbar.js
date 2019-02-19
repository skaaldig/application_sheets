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
    to: { color: '#ED6A5A' },
    step: (state, bar) => {
        bar.setText(Math.round(bar.value() * 100) + ' %');
    }
});

const getMaxStep = function () {
    const x = document.getElementById("counter").innerHTML
    const numbers = x.match(/\d+/g)
    const maxSteps = parseInt(numbers[1])
    return parseFloat(((100 / maxSteps) / 100).toFixed(5))
}

const interval = getMaxStep()

const getMinStep = function () {
    const x = document.getElementById("counter").innerHTML
    const numbers = x.match(/\d+/g)
    const minNum = parseInt(numbers[0])
    return parseFloat((minNum * interval).toFixed(5))
}

bar.animate(getMinStep());