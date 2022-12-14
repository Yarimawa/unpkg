/* eslint-disable prefer-arrow-callback, no-empty */
var printWarning = function() {};

if (process.env.NODE_ENV !== "production") {
  printWarning = function(format, subs) {
    var index = 0;
    var message =
      "Warning: " +
      (subs.length > 0
        ? format.replace(/%s/g, function() {
            return subs[index++];
          })
        : format);

    if (typeof console !== "undefined") {
      console.error(message);
    }

    try {
      // --- Welcome to debugging React Router ---
      // This error was thrown as a convenience so that you can use the
      // stack trace to find the callsite that triggered this warning.
      throw new Error(message);
    } catch (e) {}
  };
}

export default function(member) {
  printWarning(
    'Please use `import { %s } from "react-router-dom"` instead of `import %s from "react-router-dom/es/%s"`. ' +
      "Support for the latter will be removed in the next major release.",
    [member, member]
  );
}
