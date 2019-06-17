$(document).ready(function () {

    $(window).scroll(function () {

        var height = $(window).height();
        var scrollTop = $(window).scrollTop();

        if (scrollTop >= (height / 2)) {
            $('.MENU').addClass('MENU_OPACO');
            $('.nav-link').addClass('ITEM_MENU_OPACO');
        } else {
            $('.MENU').removeClass('MENU_OPACO');
            $('.nav-link').removeClass('ITEM_MENU_OPACO');
        }
    });
});