(function () {
"use strict";
var SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
$(document).ready(function(){
    $('#cart').live('click', function(){
	var asin = $(this).attr('class').split(' ')[3];
	$.ajax({
	    url: SCRIPT_ROOT + '/api' + '{{rule}}' + '/' + asin,
	    datatype: 'json',
	    error: function() {
		alert("No Dice!");
	    },
	    success: function(data) {
		console.log(data.product, data.asin);
		$.ajax({
		    type: "POST",
		    contentType: "application/json; charset=utf-8",
		    url: SCRIPT_ROOT + '/api/shopping',
		    data: JSON.stringify({"asin":data.asin, "user":"{{user.email}}", "store":data.store, "product":data.product}),
		    error: function() {
			alert("No Dice, Again!");
		    },
		    success: function(data) {
			console.log(data.product);
			},
		    dataType: 'json'
		});
	    }
	});
    }); 
});
$('#remove').live('click', function() {
	var id = $(this).attr('class').split(' ')[3];
	$.ajax({
	    type: "DELETE",
	    contentType: "application/json; charset=utf-8",
	    url: SCRIPT_ROOT + '/api/shopping/' + id,
	    success: function() {
		location.reload();
		},
	    error: function() {
		alert("No Dice, Thrice!");
	    },
	    dataType: 'json'
	});
    });
}());

