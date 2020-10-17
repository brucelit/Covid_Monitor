var ec_left1 = echarts.init(document.getElementById('l1'), "dark");

var ec_left1_Option = {
	//标题样式
	title: {
		text: "疫情统计",
		textStyle: {
			// color: 'white',
            fontSize:25,
		},
		left: '50%',

	},
	tooltip: {
		trigger: 'axis',
		//指示器
		axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
	},
	legend: {
		data: ['累计确诊', '累计输入', "累计治愈", "累计死亡"],
		left: "20",
        padding: [45, 10, 10, 10,
]
	},

	//图形位置
	grid: {
		left: '4%',
		right: '6%',
		bottom: '4%',
		top: "18%",
		containLabel: true
	},
	xAxis: [{
		type: 'category',
		//x轴坐标点开始与结束点位置都不在最边缘
		// boundaryGap : true,
		data: []//['01.20', '01.21', '01.22']
	}],
	yAxis: [{
		type: 'value',
		//y轴字体设置
		axisLabel: {
			show: true,
			color: 'white',
			fontSize: 12,
			formatter: function(value) {
				if (value >= 1000) {
					value = value / 1000 + 'k';
				}
				return value;
			}
		},
		//y轴线设置显示
		axisLine: {
			show: true
		},
		//与x轴平行的线样式
		splitLine: {
			show: true,
			lineStyle: {
				color: '#17273B',
				width: 1,
				type: 'solid',
			}
		}
	}],
	series: [{
		name: "累计确诊",
		type: 'line',
		smooth: true,
		data: []
	}, {
		name: "累计输入",
		type: 'line',
		smooth: true,
		data: []
	},
		{
		name: "累计治愈",
		type: 'line',
		smooth: true,
		data: []
	}, {
		name: "累计死亡",
		type: 'line',
		smooth: true,
		data: []
	}]
};

ec_left1.setOption(ec_left1_Option)