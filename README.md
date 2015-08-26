#Table of contents
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [TuticfrutiBootstrap3 Sublime Text Plugin](#tuticfrutibootstrap3-sublime-text-plugin)
- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [Getting Started](#getting-started)
- [Snippets](#snippets)
  - [CSS](#css)
    - [Grid system](#grid-system)
      - [Snippets](#snippets-1)
      - [Classes](#classes)
    - [Typography](#typography)
      - [Snippets](#snippets-2)
      - [Classes](#classes-1)
    - [Code](#code)
      - [Snippets](#snippets-3)
      - [Classes](#classes-2)
    - [Tables](#tables)
      - [Snippets](#snippets-4)
      - [Classes](#classes-3)
      - [Demo](#demo)
    - [Forms](#forms)
      - [Snippets](#snippets-5)
      - [Classes](#classes-4)
      - [Demo](#demo-1)
    - [Buttons](#buttons)
      - [Snippets](#snippets-6)
      - [Classes](#classes-5)
      - [Demo](#demo-2)
    - [Images](#images)
      - [Snippets](#snippets-7)
      - [Classes](#classes-6)
      - [Demo](#demo-3)
    - [Helper classes](#helper-classes)
      - [Snippets](#snippets-8)
      - [Classes](#classes-7)
      - [Demo](#demo-4)
    - [Responsive utilities](#responsive-utilities)
      - [Classes](#classes-8)
  - [Components](#components)
    - [Glyphicons](#glyphicons)
      - [Snippets](#snippets-9)
      - [Classes](#classes-9)
      - [Demo](#demo-5)
    - [Dropdowns](#dropdowns)
      - [Snippets](#snippets-10)
      - [Classes](#classes-10)
      - [Demo](#demo-6)
    - [Button groups](#button-groups)
      - [Snippets](#snippets-11)
      - [Classes](#classes-11)
      - [Demo](#demo-7)
    - [Input groups](#input-groups)
      - [Snippets](#snippets-12)
      - [Classes](#classes-12)
      - [Demo](#demo-8)
    - [Navs](#navs)
      - [Snippets](#snippets-13)
      - [Classes](#classes-13)
      - [Demo](#demo-9)
    - [Navbar](#navbar)
      - [Snippets](#snippets-14)
      - [Classes](#classes-14)
      - [Demo](#demo-10)
    - [Breadcrumb](#breadcrumb)
      - [Snippets](#snippets-15)
      - [Classes](#classes-15)
      - [Demo](#demo-11)
    - [Pagination](#pagination)
      - [Snippets](#snippets-16)
      - [Classes](#classes-16)
      - [Demo](#demo-12)
    - [Labels](#labels)
      - [Snippets](#snippets-17)
      - [Classes](#classes-17)
      - [Demo](#demo-13)
    - [Badges](#badges)
      - [Snippets](#snippets-18)
      - [Classes](#classes-18)
      - [Demo](#demo-14)
    - [Jumbotron](#jumbotron)
      - [Snippets](#snippets-19)
      - [Classes](#classes-19)
      - [Demo](#demo-15)
    - [Page header](#page-header)
      - [Snippets](#snippets-20)
      - [Classes](#classes-20)
      - [Demo](#demo-16)
    - [Tumbnails](#tumbnails)
      - [Snippets](#snippets-21)
      - [Classes](#classes-21)
      - [Demo](#demo-17)
    - [Alerts](#alerts)
      - [Snippets](#snippets-22)
      - [Classes](#classes-22)
      - [Demo](#demo-18)
    - [Progress bars](#progress-bars)
      - [Snippets](#snippets-23)
      - [Classes](#classes-23)
      - [Demo](#demo-19)
    - [Media object](#media-object)
      - [Snippets](#snippets-24)
      - [Classes](#classes-24)
      - [Demo](#demo-20)
    - [List group](#list-group)
      - [Snippets](#snippets-25)
      - [Classes](#classes-25)
      - [Demo](#demo-21)
    - [Panels](#panels)
      - [Snippets](#snippets-26)
      - [Classes](#classes-26)
      - [Demo](#demo-22)
    - [Responsive embed](#responsive-embed)
      - [Snippets](#snippets-27)
      - [Classes](#classes-27)
    - [Wells](#wells)
      - [Snippets](#snippets-28)
      - [Classes](#classes-28)
      - [Demo](#demo-23)
  - [Javascript](#javascript)
  - [Templates](#templates)
      - [Snippets](#snippets-29)
- [TODO](#todo)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# TuticfrutiBootstrap3 Sublime Text Plugin
A complete and reusable set of Bootstrap3 snippets for Sublime Text editor.

# Features
- [Bootstrap3](http://getbootstrap.com/).
- [Bootstrap3 classes auto-completion](https://github.com/tuticfruti/TuticfrutiBootstrap3/blob/master/snippets/all-classes.sublime-completions "all-classes.sublime-completions").
- [CSS snippets](http://getbootstrap.com/css/).
- [Components snippets](http://getbootstrap.com/components/)
- [Javascript snippets](http://getbootstrap.com/javascript/) (comming soon) snippets.
- Reusable components.
- [Youtube video demos](https://www.youtube.com/playlist?list=PLL0QEvkK-t2BxBobyy2C1P_JHg6zdeaMs "TuticfrutiBootstrap3 playlist").

# Pre-requisites
- Sublime text 2&3.
- Bootstrap 3.
- Package manager if you install from package manager.

# Getting Started
Installation.
    Manual installation. ZIP.
    Add repository. Local package manager.
    From packages.io. Install package manager.


How to use.
    Two types of snippets: classes snippets (into tag element double quotes) and component snippets (into html document, not into tag element).

    Alt + / (Edit > Show Completions menu option)

All component snippets begins with 'b' (Bootstrap) key. Class snippets are Bootstrap class literals.

Examples:

# Snippets

## CSS
### Grid system
Bootstrap includes a responsive, mobile first fluid grid system that appropriately scales up to 12 columns as the device or viewport size increases.

####Snippets
| Snippet                     | Tab trigger          |
| --------------------------- | -------------------- |
| Container & fluid container | `bcontainer`         |
| Grid row                    | `brow`               |
| Grid column                 | `bcol`               |

####Classes
- `container`
- `container-fluid`
- `row`
- `col`
- `col-(xs|sm|md|lg)-(1-12)`
- `col-(xs|sm|md|lg)-push-(1-12)`
- `col-(xs|sm|md|lg)-pull-(1-12)`
- `col-(xs|sm|md|lg)-offset-(1-12)`

### Typography

####Snippets
| Snippet                      | Tab trigger |
| ---------------------------- | ------------|
| Headings                     | `btexth`    |
| Lead body copy               | `btextle`   |
| Marked text                  | `btextm`    |
| Small text                   | `btexts`    |
| Alignment classes            | `btexta`    |
| Transformation classes       | `btextt`    |
| Initialism                   | `btexti`    |
| Blockquote with footer       | `btextb`    |
| Lists (unstyled|inline)      | `btextli`   |
| Horizontal description list  | `btexthd`   |

####Classes
- `h(1-6)`
- `lead`
- `mark`
- `small`
- `text-(left|center|right|justify|nowrap)`
- `text-(lowercase|uppercase|capitalize)`
- `initialism`
- `blockquote-reverse`
- `list-(style|unstyled|inline)`
- `dl-horizontal`

### Code

####Snippets
| Snippet           | Tab trigger |
| ----------------- | ------------|
| Block scrollable  | `bcodebs`   |

####Classes
- `pre-scrollable`

### Tables

####Snippets
| Snippet           | Tab trigger |
| ----------------- | ------------|
| Default table     | `btabled`   |
| Responsive table  | `btabler`   |
| Table row         | `btr`       |
| Table td          | `btd`       |
| Table th          | `bth`       |

####Classes
- `table`
- `table-responsive`
- `table-stripped`
- `table-bordered`
- `table-hover`
- `table-condensed`
- `active|success|info|warning|danger`

####Demo
[Tables demo](https://youtu.be/6pzlxSeV8Ik).

### Forms

####Snippets
| Snippet                 | Tab trigger |
| ----------------------- | ------------|
| Default form            | `bformd`    |
| Default form group      | `bformg`    |
| Input control           | `bctrli`    |
| Inline input control    | `bctrlii`   | 
| Textarea control        | `bctrlt`    |
| Radio control           | `bctrlr`    |
| Inline Radio control    | `bctrlri`   |
| Checkbox control        | `bctrlc`    |
| Inline checkbox control | `bctrlci`   |
| Select control          | `bctrlse`   |
| Inline select control   | `bctrlsei`  |
| Static control          | `bctrlst`   |
| Inline static control   | `bctrlsti`  |
| Submit button           | `bctrlsu`   |
| Inline submit button    | `bctrlsui`  |
| Help text               | `bctrlht`   |
| Label                   | `bctrll`    |
| Inline Label            | `bctrlli`   |
| Field set               | `bformf`    |

####Classes
- `form-inline`
- `form-horizontal`
- `form-group`
- `form-group-(sm|lg)`
- `form-control`
- `text|password|datetime|date|month|time|week|number|email|url|search|tel|color|datetime-local`
- `radio`
- `checkbox`
- `control-label`
- `form-control-static`
- `active`
- `desabled`
- `readonly`
- `has-(success|warning|error)`
- `input(sm|lg)`
- `help-block`

####Demo
[Forms demo](https://youtu.be/8V3Imk1gRKk).

### Buttons

####Snippets
| Snippet           | Tab trigger |
| ----------------- | ------------|
| Default button    | `bbtnd`     |
| Link button       | `bbtnl`     |

####Classes
- `btn`
- `btn-(default|primary|success|info|warning|danger|link)`
- `btn-(xs|sm|lg)`
- `btn-block`
- `active`
- `disabled`

####Demo
[Buttons demo](https://youtu.be/Yj83bzlKlNU).

### Images

####Snippets
| Snippet           | Tab trigger |
| ----------------- | ------------|
| Default image     | `bimaged`   |

####Classes
- `img-responsive`
- `img-rounded`
- `img-circle`
- `img-thumbnail`

####Demo
[Images demo](https://youtu.be/P6F72Ju-fnU).

### Helper classes

####Snippets
| Snippet                | Tab trigger  |
| ---------------------- | -------------|
| Contextual colors      | `bhelperco`  |
| Contextual backgrounds | `bhelperb`   |
| Close icon             | `bhelperci`  |
| Carets                 | `bhelperca`  |
| Quick floats           | `bhelperf`   |
| Center content blocks  | `bhelpercb`  |
| Clearfix               | `bhelpercl`  |
| Showing and hiding     | `bhelperv`   |
| Screen reader default  | `bhelpersrd` |
| Screen reader link     | `bhelpersrl` |

####Classes
- `text-(muted|primary|success|info|warning|danger)`
- `bg-(primary|success|info|warning|danger)`
- `caret`
- `pull-(left|right)`
- `center-block`
- `clearfix`
- `show|hidden`
- `sr-only`
- `sr-only-focusable`
- `text-hide`

####Demo
[Helpers demo](https://youtu.be/S2AzJ9Z5OFc).

### Responsive utilities
For faster mobile-friendly development, use these utility classes for showing and hiding content by device via media query. Also included are utility classes for toggling content when printed.

####Classes
- `visible-(xs|sm|md|lg)`
- `visible-(xs|sm|md|lg)-block`
- `visible-(xs|sm|md|lg)-inline`
- `visible-(xs|sm|md|lg)-inline-block`
- `hidden-(xs|sm|md|lg)`
- `visible-print-(block|inline|inline-block)`
- `hidden-print`

## Components

### Glyphicons
Includes over 250 glyphs in font format from the Glyphicon Halflings set ([Glyphicons homepage](http://glyphicons.com/)).

####Snippets
| Snippet           | Tab trigger          |
| ----------------- | -------------------- |
| Default glyphicon | `bglyphicon-default` |
| Glyphicon button  | `bbutton-glyphicon`  |

####Classes
- `glyphicon`
- `glyphicon-(home|user|star|exclamation-sign|...)`

####Demo
[Glyphicons demo](https://youtu.be/u9JYaSSVgUM).

### Dropdowns
Toggleable, contextual menu for displaying lists of links. Made interactive with the dropdown JavaScript plugin.

#### Snippets
| Snippet                | Tab trigger               |
| ---------------------- | ------------------------- |
| Default dropdown       | `bdropdown-default`       |
| Default dropdown item  | `bbutton-glyphicon`       |
| Header dropdown item   | `bdropdown-item-header`   |
| Divider dropdown item  | `bdropdown-item-divider`  |
| Active dropdown item   | `bdropdown-item-active`   |
| Disabled dropdown item | `bdropdown-item-disabled` |

####Classes
- `dropdown`
- `dropup`
- `dropdown-menu`
- `dropdown-menu-left`
- `dropdown-menu-right`
- `dropdown-header`
- `active`
- `disabled`
- `divider`
- `separator`

####Demo
[Dropdowns demo](https://youtu.be/3w0m4IR4kEY).

### Button groups
Group a series of buttons together on a single line with the button group. For more complex components, combine sets of button groups into a button toolbar.

#### Snippets
| Snippet                | Tab trigger               |
| ---------------------- | ------------------------- |
| Default button group   | `bbutton-group-default`   |
| Justified button group | `bbutton-group-justified` |
| Button toolbar         | `bbutton-toolbar`         |

#### Classes
- `btn-group`
- `btn-toolbar`
- `btn-group-(xs|sm|lg)`
- `btn-group-vertical`
- `btn-group-justified`

#### Demo
[Button groups demo](https://youtu.be/BgqjRGxhD-4).

### Input groups
Extend form controls by adding text or buttons before, after, or on both sides of any text-based `<input>`. 

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default input group            | `binput-group-default`        |
| Checkboxes and radio addon     | `binput-group-radio-checkbox` |
| Button with dropdown           | `binput-group-dropdown`       |
| Button addon                   | `binput-group-button`         |
| Segmented buttons              | `binput-group-split`          |

#### Classes
- `input-group`
- `input-group-addon`
- `input-group-(sm|lg)`
- `input-group-btn`

#### Demo
[Input groups demo](https://youtu.be/-Hj7GBi3Ecs).

### Navs

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default nav                    | `bnav-default`                |
| Default nav item               | `bnav-item-default`           |
| Active nav item                | `bnav-item-active`            |
| Disabled nav item              | `bnav-item-disable`           |

#### Classes
- `nav`
- `nav-(tabs|pills)`
- `nav-stacked`
- `nav-justified`
- `active|disabled`

#### Demo
[Nav demo](https://youtu.be/LRAFHiGdSew).

### Navbar
Navbars are responsive meta components that serve as navigation headers for your application or site.

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default navbar                 | `bnavbar-default`             |
| Navbar button item             | `bnavbar-item-button`         |
| Navbar divider item            | `bnavbar-item-divider`        |
| Navbar dropdown item           | `bnavbar-item-dropdown`       |
| Navbar link item               | `bnavbar-item-link`           |
| Navbar text item               | `bnavbar-item-text`           |
| Navbar form item               | `bnavbar-item-form`           |
| Navbar Brand image item        | `bnavbar-item-brand-image`    |

#### Classes
- `navbar`
- `bavbar-default`
- `navbar-header`
- `navbar-toggle`
- `collapsed`
- `icon-bar`
- `navbar-brand`
- `navbar-nav`
- `divider`
- `navbar-(left|right)`
- `navbar-btn`
- `navbar-text`
- `navbar-fixed-(top|bottom)`
- `navbar-static-top`
- `navbar-inverse`

#### Demo
[Navbar demo](https://youtu.be/E-7GAsUgx7Y).

### Breadcrumb

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default breadcrumb             | `bbreadcrumb-default`         |
| Default breadcrumb item        | `bbreadcrumb-item-default`    |
| Active breadcrumb item         | `bbreadcrumb-item-active`     |

#### Classes
- `breadcrumb`
- `active`

#### Demo
[Breadcrumb demo](https://youtu.be/Y3a1nW6Xztc).

### Pagination
Provide pagination links for your site or app with the multi-page pagination component, or the simpler pager alternative.

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default pagination             | `bpagination-default`         |
| Default pagination item        | `bpagination-item-default`    |
| Active pagination item         | `bpagination-item-active`     |
| Disabled pagination item       | `bpagination-item-disable`    |
| Pager                          | `bpagination-pager`         |

#### Classes
- `pagination`
- `pagination-(sm|lg)`
- `active|disabled`
- `pager`
- `previous|next`

#### Demo
[Pagination demo](https://youtu.be/t9RukSB-kqQ).

### Labels

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default label                  | `blabel-default`              |
| Inline label                   | `blabel-inline`               |

#### Classes
- `label`
- `label-(default|primary|success|info|warning|danger)`

#### Demo
[Labels demo](https://youtu.be/T0VwT39qNH4).

### Badges

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Button badge                   | `bbadge-button`               |
| Link badge                     | `bbadge-link`                 |

#### Classes
- `badge`
- `active`

#### Demo
[Badges demo](https://youtu.be/xZCCkxFu_40).

### Jumbotron

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Jumbotron                      | `bjumbotron`                  |

#### Classes
- `jumbotron`

#### Demo
[Jumbotron demo](https://youtu.be/lqlq9XrxEgY).

### Page header

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default page header                    | `bpage-header`                |


#### Classes
- `page-header`

#### Demo
[Page headers demo](https://youtu.be/gKTKujmXjKU).

### Tumbnails
Extend Bootstrap's grid system with the thumbnail component to easily display grids of images, videos, text, and more.

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default thumbnail              | `bthumbnail-default`          |

#### Classes
- `thumbnail`

#### Demo
[Thumbnails demo](https://youtu.be/MK-CwiG3LW0).

### Alerts
Provide contextual feedback messages for typical user actions with the handful of available and flexible alert messages.

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default alert                  | `balert-default`              |
| Dismissible alert              | `balert-dismissible`          |
| Alert link                     | `balert-link`                 |

#### Classes
- `alert`
- `alert-(success|info|warning|danger)`
- `alert-dismissible`
- `alert-link`

#### Demo
[Alerts demo](https://youtu.be/JkR88QLstZw).

### Progress bars
Provide up-to-date feedback on the progress of a workflow or action with simple yet flexible progress bars.

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default progress bar           | `bprogress-bar-default`       |
| Stacked progress bars          | `bprogress-bar-stack`         |

#### Classes
- `progress`
- `progress-bar`
- `progress-bar-(success|info|warning|danger)`
- `progress-bar-striped`
- `active` (animated)

#### Demo
[Progress bars demo](https://youtu.be/DDp_lvrUxSw).

### Media object

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default media                  | `bmedia-default`              |
| Media item                     | `bmedia-item-default`         |

#### Classes
- `media`
- `media-(left|right)`
- `media-object`
- `media-body`
- `media-heading`
- `media-list`

#### Demo
[Media object demo](https://youtu.be/4iHBV06jGC4).

### List group
List groups are a flexible and powerful component for displaying not only simple lists of elements, but complex ones with custom content.

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default list group             | `blist-group-default`         |
| Default item                   | `blist-group-item-default`    |
| Badge item                     | `blist-group-item-badge`      |
| Button item                    | `blist-group-item-button`     |
| Link item                      | `blist-group-item-link`       |
| Context item                   | `blist-group-item-context`    |
| Custom item                    | `blist-group-item-custom`     |


#### Classes
- `list-group`
- `list-group-item`
- `badge`
- `active|disabled`
- `list-group-item-(success|info|warning|danger)`
- `list-group-item-heading`
- `list-group-item-text`

#### Demo
[List groups demo](https://youtu.be/zDB_pL3-IqE).

### Panels
While not always necessary, sometimes you need to put your DOM in a box. For those situations, try the panel component.

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default panel                  | `bpanel-default`              |

#### Classes
- `panel`
- `panel-heading`
- `panel-footer`
- `panel-title`
- `panel-(default|primary|success|info|warning|danger)`

#### Demo
[Panels demo](https://youtu.be/AFYFt8Wja_U).

### Responsive embed

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Responsive embed               | `bembed-responsive`           |

#### Classes
- `embed-responsive`
- `embed-responsive-item`
- `embed-responsive-16by9`
- `embed-responsive-4by3`

### Wells

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default well                   | `bwell-default`               |

#### Classes
- `well`
- `well-(sm|lg)`

#### Demo
[Well demo](https://youtu.be/HDwzV6NJpCo).

## Javascript
Comming soon.

## Templates

#### Snippets
| Snippet                        | Tab trigger                   |
| ------------------------------ | ----------------------------- |
| Default template               | `btemplate-default`           |

#TODO
- Javascript Bootstrap3 support.

# License
**The MIT License (MIT)**

**Copyright (c) 2015 tuticfruti**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
