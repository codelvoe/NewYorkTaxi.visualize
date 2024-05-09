var myChart = echarts.init(document.querySelector(".map .map4"));

var option = {
    backgroundColor: 'rgba(0, 0, 0, 0)',
    tooltip: {
        trigger: 'item',
        formatter: '{b}: {c}'
    },
    visualMap: {
        min: 5000,
        max: 10000000,
        calculable: true,
        inRange: {
            color: ['#FFFF00','#FFA500']
        },
        textStyle: {
            color: '#fff'
        },
        show:false
        // left: 'left', // 调整 visualMap 的水平位置
        // top: 'bottom', // 调整 visualMap 的垂直位置，这里放置在地图的上方
        // align: 'auto' // 让 visualMap 自动与地图对齐
    },
    geo: {
        map: "nyc",
        roam: false,
        zoom: 1,
        itemStyle: {
            normal: {
                areaColor: "rgba(43, 196, 243, 0.42)",
                borderColor: "rgba(43, 196, 243, 1)",
                borderWidth: 1
            },
            emphasis: {
                areaColor: "#fff"
            }
        }
    },
    series: [{
        type: 'map',
        map: 'nyc',
        data: [{
                name: 'Manhattan',
                value: 95007975
            },
            {
                name: 'Brooklyn',
                value: 4087162
            },
            {
                name: 'Queens',
                value: 9010929
            },
            {
                name: 'The Bronx',
                value: 666404
            },
            {
                name: 'Staten Island',
                value: 4800
            }
        ],
        label: {
            show: true,
            textStyle: {
                color: '#000'
            }
        },
        emphasis: {
            areaColor: "#1E90FF",
            label: {
                show: true
            }
        },
        itemStyle: {
            opacity: 0.7
        },
        select: {
            show: true
        }
    }]
};

myChart.setOption(option);
window.addEventListener("resize", function() {
    myChart.resize();
});
