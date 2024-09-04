// handle dark and light mode
function change_mode(check) {
    // update bar chart
    if (document.getElementById("stats") && check === 0) {
        update_chart()
    }
  // when it's light mode
  if (localStorage.getItem("dark") === "false") {
    console.log("LIGHT MODE")

    // update rest of the elements
    document.querySelectorAll("*").forEach(function (element) {
      element.style.color = "black"

      if (element.tagName === "INPUT") {
        element.style.border = "1px solid black"
        element.style.fontFamily = "'Courier New', Courier, monospace"
      }

      // if it's a table
      if (element.tagName === "TH" || element.tagName === "TD") {
        // outline it in a different color
        element.style.border = "1px solid black"
        element.style.fontFamily = "'Courier New', Courier, monospace"
      }
    })
    return true
  }
  // when it's dark mode
  else {
    console.log("DARK MODE")

    // update rest of the elements
    document.querySelectorAll("*").forEach(function (element) {
      element.style.color = "white"

      if (element.tagName == "INPUT") {
        element.style.border = "1px solid white"
        element.style.fontFamily = "'Courier New', Courier, monospace"
      }

      // if it's a table
      if (element.tagName === "TH" || element.tagName === "TD") {
        // outline it in a different color
        element.style.border = "1px solid white"
        element.style.fontFamily = "'Courier New', Courier, monospace"
      }
    })
    return false
  }
}
