$.CafePerfeito = {};

function clicked(e) {
    if (!confirm('Are you sure?')) e.preventDefault();
}

/* Searchbar - Function ================================================================================================
*  You can manage the search bar
*
*/
// var $searchBar = $('.search-bar');
// $.CafePerfeito.search = {
//     activate: function () {
//         var _this = this;
//
//         //Search button click event
//         $('.js-search').on('click', function () {
//             _this.showSearchBar();
//         });
//
//         //Close search click event
//         $searchBar.find('.close-search').on('click', function () {
//             _this.hideSearchBar();
//         });
//
//         //ESC key on pressed
//         $searchBar.find('input[type="text"]').on('keyup', function (e) {
//             if (e.keyCode == 27) {
//                 _this.hideSearchBar();
//             }
//         });
//     },
//     showSearchBar: function () {
//         $searchBar.addClass('open');
//         $searchBar.find('input[type="text"]').focus();
//         // showMsg("estou no SearchBar")
//     },
//     hideSearchBar: function () {
//         $searchBar.removeClass('open');
//         $searchBar.find('input[type="text"]').val('');
//         // showMsg("estou no SearchBar")
//     }
// }
//==========================================================================================================================

// $(function () {
//     // $.CafePerfeito.browser.activate();
//     // $.CafePerfeito.leftSideBar.activate();
//     // $.CafePerfeito.rightSideBar.activate();
//     // $.CafePerfeito.navbar.activate();
//     // $.CafePerfeito.dropdownMenu.activate();
//     // $.CafePerfeito.input.activate();
//     // $.CafePerfeito.select.activate();
//     $.CafePerfeito.search.activate();
//
//     setTimeout(function () {
//         $('#logo').fadeOut();
//     }, 1000);
// });

(function () {
    var pwd = document.getElementById('password');
    var chk = document.getElementById('showPassword');

    chk.addEventListener('change', function (e) {
        var target = e.target || e.srcElement;
        try {
            if (target.checked) {
                pwd.type = 'text';
            } else {
                pwd.type = 'password';
            }
        } catch (error) {
            alert('não é possivel mudar o tipo')
        }
    });
}());







