import QtQuick 2.1
import QtQuick.Controls 1.1

/**
 * This is a workaround for lacking API in the QtQuick Controls MenuBar.
 * It replicates some of the functionality included in QtQuick Controls'
 * ApplicationWindow class to make the menu bar actually work.
 */
Rectangle {
    id: menuBackground;

    property QtObject window;
    Binding {
        target: menu.__contentItem;
        property: "width";
        value: window.width;
        when: !menu.__isNative;
    }

    default property alias menus: menu.menus

    width: menu.__isNative ? 0 : menu.__contentItem.width
    height: menu.__isNative ? 0 : menu.__contentItem.height

    color: palette.window;

    Keys.forwardTo: menu.__contentItem;

    MenuBar {
        id: menu

        //__parentWindow: menuBackground.window

        Component.onCompleted: {
            __contentItem.parent = menuBackground;
        }
    }

    SystemPalette { id: palette; colorGroup: SystemPalette.Active }
}
