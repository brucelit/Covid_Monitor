function gettime() {
    $.ajax({
        url: "/time",
        timeout: 1000, //超时时间设置为10秒；
        success: function(data) {
            $("#tim").html(data)
        },
        error: function(xhr, type, errorThrown) {

        }
    });
}
function get_c1_data() {
    $.ajax({
        url: "/c1",
        success: function(data) {
            $(".num h1").eq(0).text(data.confirm);
            $(".num h1").eq(1).text(data.import_case);
            $(".num h1").eq(2).text(data.heal);
            $(".num h1").eq(3).text(data.dead);
            $(".num h1").eq(4).text(data.suspect);
            $(".num h1").eq(5).text(data.heal_rate);
            $(".num h1").eq(6).text(data.dead_rate);
        },
        error: function(xhr, type, errorThrown) {

        }
    })
}

function get_l1_data() {
    $.ajax({
        url:"/l1",
        success: function(data) {
			ec_left1_Option.xAxis[0].data=data.day
            ec_left1_Option.series[0].data=data.confirm
            ec_left1_Option.series[1].data=data.import_case
            ec_left1_Option.series[2].data=data.heal
            ec_left1_Option.series[3].data=data.dead
            ec_left1.setOption(ec_left1_Option)
		},
		error: function(xhr, type, errorThrown) {

		}
    })
}
gettime()
get_c1_data()
get_l1_data()
setInterval(get_c1_data,1000)
setInterval(gettime,1000)
setInterval(get_l1_data,1000)