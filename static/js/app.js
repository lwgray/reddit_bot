(function() {
    "use strict";
    $(document).ready(function() {
      $("#cart").click(function() {
        var asin = $("#cart").val();
        $.ajax({
          url: $SCRIPT_ROOT + '/api/mattel/' + asin,
          dataType: 'json',
          error: function() {
            alert("No more people.");
          },
          success: function(data) {
                $.ajax({
                type: "POST",
                contentType: "application/json; charset=utf-8",  
                url: $SCRIPT_ROOT + '/api/shoppinglist',
                data: {"user":{{user.email}}, "store":data.store, "product":data.product, "asin":data.asin},
                success: function(data) {
                   console.log(data.product);
                }, 
                dataType:'json'
            });
          };
        });
      });
    });
