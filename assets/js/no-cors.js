window.onerror = function(errorMsg, file, lineNo, colNo, errStack) {
    "use strict";
    var msg = errorMsg ? errorMsg : "null"
    , stack = errStack ? errStack : "null, only Chromium based browsers support errorStack"
    ;
    $("#msg").html(msg);
    $("#stack").html(stack);
};

window.clickMe = function() {
    "use strict";
    var l = "test";
    l.callme();
};
