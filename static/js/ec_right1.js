var ec_right1 = echarts.init(document.getElementById('r1'), "dark");

var ec_right1_Option = {
	//标题样式
	title: {
		text: "疫情趋势",
		textStyle: {
			// color: 'white',
            fontSize:25,
		},
		left: '45%',

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
		data: ['新增确诊', '新增死亡'],
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
		name: "新增确诊",
		type: 'line',
		smooth: true,
		data: []
	}, {
		name: "新增死亡",
		type: 'line',
		smooth: true,
		data: []
	}]
};

ec_right1.setOption(ec_right1_Option)