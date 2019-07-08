$(function() {
    // $('.notes-dialog').hide()
  
    $('.ingredient, .direction').click(function() {
        if( $(this).css("text-decoration-line") == 'none' ) {
            $(this).css("text-decoration-line", "line-through");
        } else {
            $(this).css("text-decoration-line", "none");
        }
    });

    // $('#open-notes').click(function() {
    //   $('.notes-dialog').show(500)
    // })
  
    // $('#form p button').click(function() {
    //   $('.notes-dialog').hide(500)
    // })
  
    // $('#close-notes').click(function() {
    //   $('.notes-dialog').hide(500)
    // })
});

function toggleMobileOrder() {
    div = $('#recipe-main')
    if( div.css('flex-direction') == 'column' ) {
        div.css('flex-direction', 'column-reverse');
    } else {
        div.css('flex-direction', 'column');
    }
    
}