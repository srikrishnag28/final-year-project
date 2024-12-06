// Loading
$(function() {
	$("#loading-wrapper").fadeOut(1000);
});


// Toggle sidebar
$("#toggle-sidebar").on('click', function () {
	$(".page-wrapper").toggleClass("toggled");
});


// Toggle sidebar togglescreen
$("#sidebar-togglescreen").on('click', function () {
	$(".page-wrapper.togglescreen").toggleClass("toggled-togglescreen");
});


jQuery(function ($) {
    // Toggle the main sidebar dropdown and arrow
    $(".sidebar-dropdown > a").on('click', function (e) {
        if ($(e.target).is("i")) {
            var submenu = $(this).next(".sidebar-submenu");
            var icon = $(this).find("i");

            // Toggle the submenu visibility
            submenu.slideToggle(200);
            $(this).parent().toggleClass("active");

            // Toggle the icon class
            if (icon.hasClass("bi-caret-down")) {
                icon.removeClass("bi-caret-down").addClass("bi-caret-up-fill");
            } else {
                icon.removeClass("bi-caret-up-fill").addClass("bi-caret-down");
            }
        }
    });

    // Toggle the sub-sidebar dropdown and arrow
    $(".sub-sidebar-dropdown > a").on('click', function (e) {
        if ($(e.target).is("i")) {
            var subsubmenu = $(this).next(".sub-sidebar-submenu");
            var subIcon = $(this).find("i");

            // Toggle the sub-submenu visibility
            subsubmenu.slideToggle(200);
            $(this).parent().toggleClass("active");

            // Toggle the icon class for sub-menu
            if (subIcon.hasClass("bi-caret-down")) {
                subIcon.removeClass("bi-caret-down").addClass("bi-caret-up-fill");
            } else {
                subIcon.removeClass("bi-caret-up-fill").addClass("bi-caret-down");
            }
        }
    });
});



// Toggle graph day selection
$(function() {
	$(".graph-day-selection .btn").on('click', function () {
		$(".graph-day-selection .btn").removeClass("active");
		$(this).addClass("active");   
	});
});


// Download File
$('.download-reports').on('click', function () {
	$.ajax({
		url: 'sample.txt',
		crossOrigin: null,
		xhrFields: {
		responseType: 'blob'
		},
		success: function(blob) {
		console.log(blob.size);
		var link = document.createElement('a');
		link.href = window.URL.createObjectURL(blob);
		link.download = "Reports" + ".txt";
		link.click();
		}
	});
});



// Todays Date
$(function() {
	var interval = setInterval(function() {
		var momentNow = moment();
		$('.todaysDate').html(momentNow.format('LLLL'));
	}, 100);
});



// Toggle Pricing Plan
$(".pricing-change-plan a").on('click', function () {
	if ($(this).hasClass("active-plan")) {
	  $(".pricing-change-plan a").removeClass("active-plan");
	}
	else {
	  $(".pricing-change-plan a").removeClass("active-plan");
	  $(this).addClass("active-plan");
	}
});


/***********
***********
***********
	Bootstrap JS 
***********
***********
***********/

// Tooltip
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
	return new bootstrap.Tooltip(tooltipTriggerEl)
})

// Popover
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
	return new bootstrap.Popover(popoverTriggerEl)
})




