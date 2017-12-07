$(document).ready(function () {
    $('#cart').click(function () {
        var asin = $(this).attr('class').split(' ')[3];
        var url = '/api' + '/toysrus' + '/' + asin;
        var url2 = '/api' + '/shopping';
        $.ajax({
            url: url,
            dataType: "json",
            success: function (data) {
                $.ajax({
                    url: url2,
                    data: JSON.stringify({
                        "asin": data.asin,
                            "user": "{{user.email}}",
                            "store": data.store,
                            "product": data.product
                    }),
                    type: "POST",
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    success: function () {
                        alert("added " + asin + " to shopping cart");
                    }
                });
            }
        });
    });
});
