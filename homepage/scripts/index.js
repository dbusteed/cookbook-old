$(function(context) {
    return function() {
        // init    
        let page_num = 1;
        let num_pages = context.num_pages;

        // localStorage.setItem("search", context.search);
        // localStorage.setItem("cat_id", context.cat_id);
        // localStorage.setItem("my_rec", context.my_rec);

        console.log(context);

        $('#recipes').load( `/homepage/index.recipes/${page_num}/${context.my_rec}/${(context.search) ? context.search : ''}/${(context.cat_id) ? context.cat_id : 0}`);

        if(num_pages <= 1) {
            $('.pag-button').hide();
        }

        $('.next').click( () => {
            page_num++;
            if(page_num == num_pages) {
                $('.next').hide();
            }
            if(page_num == 2) {
                $('.prev').show();
            }
            $('#recipes').load( `/homepage/index.recipes/${page_num}/False/${(context.search) ? context.search : ''}/${(context.cat_id) ? context.cat_id : 0}`);
            $('#page-num').text(page_num);
        });
        
        $('.prev').click( () => {
            page_num--;
            if(page_num == 1) {
                $('.prev').hide();
            }
            if(page_num == num_pages-1) {
                $('.next').show();
            }
            $('#recipes').load( `/homepage/index.recipes/${page_num}/False/${(context.search) ? context.search : ''}/${(context.cat_id) ? context.cat_id : 0}`);
            $('#page-num').text(page_num);
        });

        $('#switch').change( () => {

            if( $('#switch').is(':checked') ) {
                document.getElementById("my_rec").value = "True";
                document.getElementById("category-filter").submit();
            } else {
                document.getElementById("my_rec").value = "False";
                document.getElementById("category-filter").submit();
            }      
        });

        // $('body').click( () => {
        //     console.log('body');
        //     if( $('.dropdown-menu-full').css('display') != 'none' ) {
        //         console.log('not none!');
        //         $('.dropdown-menu-full').css('display', 'none');
        //     }
        // })
    }
}(DMP_CONTEXT.get()));

function selectCategory(cat_id) {
    document.getElementById("cat_id").value = cat_id;
    document.getElementById("category-filter").submit();
}

function miniMenuRecToggle() {
    if( $('#switch').is(':checked') ) {
        document.getElementById("my_rec").value = "False";
        document.getElementById("category-filter").submit();
        $('#switch').prop('checked', false)
    } else {
        document.getElementById("my_rec").value = "True";
        document.getElementById("category-filter").submit();
        $('#switch').prop('checked', true)
    }
}

