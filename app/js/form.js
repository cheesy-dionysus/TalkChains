var addToLog = function(txt){
    $(.log).append("<br>" + txt);
}

$(document).ready(function() {
    $(button.set).click(function(){
        var rec = $("input.hash").val();
        var h_id = parseInt($("input.hid").val(), 10);
        var u_id = $("input.uid").val();
        userContrat.uploadRecords()
    });
});