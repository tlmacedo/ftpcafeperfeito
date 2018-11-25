// var $ = django.jQuery;
$.CafePerfeito = {};

/* Searchbar - Function ================================================================================================
*  You can manage the search bar
*
*/
var $searchBar = $('.search-bar');
$.CafePerfeito.search = {
    activate: function () {
        var _this = this;

        //Search button click event
        $('.js-search').on('click', function () {
            _this.showSearchBar();
        });

        //Close search click event
        $searchBar.find('.close-search').on('click', function () {
            _this.hideSearchBar();
        });

        //ESC key on pressed
        $searchBar.find('input[type="text"]').on('keyup', function (e) {
            if (e.keyCode == 27) {
                _this.hideSearchBar();
            }
        });
    },
    showSearchBar: function () {
        $searchBar.addClass('open');
        $searchBar.find('input[type="text"]').focus();
    },
    hideSearchBar: function () {
        $searchBar.removeClass('open');
        $searchBar.find('input[type="text"]').val('');
    }
}
//==========================================================================================================================


$(function () {
    $.CafePerfeito.search.activate();
    // $.SIDTM.browser.activate();
    // $.SIDTM.leftSideBar.activate();
    // $.SIDTM.rightSideBar.activate();
    // $.SIDTM.navbar.activate();
    // $.SIDTM.dropdownMenu.activate();
    // $.SIDTM.input.activate();
    // $.SIDTM.select.activate();

    setTimeout(function () {
        $('#logo').fadeOut();
    }, 30000);
});
