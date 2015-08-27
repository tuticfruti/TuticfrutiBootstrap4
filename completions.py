import sublime_plugin

SCOPE = 'text.html meta.tag string.quoted.double'
COMPLETIONS = [
    ('container\tbclass', 'container'),
    ('container-fluid\tbclass', 'container-fluid'),
    ('row\tbclass', 'row'),
    ('col-xs\tbclass', 'col-xs'),
    ('col-sm\tbclass', 'col-sm'),
    ('col-md\tbclass', 'col-md'),
    ('col-lg\tbclass', 'col-lg'),
    ('col-xl\tbclass', 'col-xl'),
    ('col-xs-offset\tbclass', 'col-xs-offset'),
    ('col-sm-offset\tbclass', 'col-sm-offset'),
    ('col-md-offset\tbclass', 'col-md-offset'),
    ('col-lg-offset\tbclass', 'col-lg-offset'),
    ('col-xl-offset\tbclass', 'col-xl-offset'),
    ('col-xs-push\tbclass', 'col-xs-push'),
    ('col-sm-push\tbclass', 'col-sm-push'),
    ('col-md-push\tbclass', 'col-md-push'),
    ('col-lg-push\tbclass', 'col-lg-push'),
    ('col-xl-push\tbclass', 'col-xl-push'),
    ('col-xs-pull\tbclass', 'col-xs-pull'),
    ('col-sm-pull\tbclass', 'col-sm-pull'),
    ('col-md-pull\tbclass', 'col-md-pull'),
    ('col-lg-pull\tbclass', 'col-lg-pull'),
    ('col-xl-pull\tbclass', 'col-xl-pull'),
    ('media\tbclass', 'media'),
    ('media-left\tbclass', 'media-left'),
    ('media-object\tbclass', 'media-object'),
    ('media-body\tbclass', 'media-body'),
    ('media-heading\tbclass', 'media-heading'),
    ('media-top\tbclass', 'media-top'),
    ('media-middle\tbclass', 'media-middle'),
    ('media-bottom\tbclass', 'media-bottom'),
    ('media-list\tbclass', 'media-list'),
    ('hidden-xs-up\tbclass', 'hidden-xs-up'),
    ('hidden-sm-up\tbclass', 'hidden-sm-up'),
    ('hidden-md-up\tbclass', 'hidden-md-up'),
    ('hidden-lg-up\tbclass', 'hidden-lg-up'),
    ('hidden-xl-up\tbclass', 'hidden-xl-up'),
    ('hidden-xs-down\tbclass', 'hidden-xs-down'),
    ('hidden-sm-down\tbclass', 'hidden-sm-down'),
    ('hidden-md-down\tbclass', 'hidden-md-down'),
    ('hidden-lg-down\tbclass', 'hidden-lg-down'),
    ('hidden-xl-down\tbclass', 'hidden-xl-down'),
    ('visible-print-block\tbclass', 'visible-print-block'),
    ('visible-print-inline\tbclass', 'visible-print-inline'),
    ('visible-print-inline-block\tbclass', 'visible-print-inline-block'),
    ('hidden-print\tbclass', 'hidden-print'),
    ('h1\tbclass', 'h1'),
    ('h2\tbclass', 'h2'),
    ('h3\tbclass', 'h3'),
    ('h4\tbclass', 'h4'),
    ('h5\tbclass', 'h5'),
    ('h6\tbclass', 'h6'),
    ('display-1\tbclass', 'display-1'),
    ('display-2\tbclass', 'display-2'),
    ('display-3\tbclass', 'display-3'),
    ('display-4\tbclass', 'display-4'),
    ('text-muted\tbclass', 'text-muted'),
    ('lead\tbclass', 'lead'),
    ('initialism\tbclass', 'initialism'),
    ('blockquote-reverse\tbclass', 'blockquote-reverse'),
    ('list-unstyled\tbclass', 'list-unstyled'),
    ('list-inline\tbclass', 'list-inline'),
    ('dl-horizontal\tbclass', 'dl-horizontal'),
    ('text-truncate\tbclass', 'text-truncate'),
    ('pre-scrollable\tbclass', 'pre-scrollable'),
    ('text-left\tbclass', 'text-left'),
    ('text-right\tbclass', 'text-right'),
    ('text-center\tbclass', 'text-center'),
    ('text-justify\tbclass', 'text-justify'),
    ('text-nowrap\tbclass', 'text-nowrap'),
    ('pull-left\tbclass', 'pull-left'),
    ('pull-right\tbclass', 'pull-right'),
    ('center-block\tbclass', 'center-block'),
    ('table\tbclass', 'table'),
    ('table-inverse\tbclass', 'table-inverse'),
    ('table-striped\tbclass', 'table-striped'),
    ('table-bordered\tbclass', 'table-bordered'),
    ('thead-inverse\tbclass', 'thead-inverse'),
    ('thead-default\tbclass', 'thead-default'),
]


class ExampleCommand(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):

        current_point = locations[0]

        if view.match_selector(current_point, SCOPE):

            current_line_region = view.line(current_point)
            class_region = view.find('class=\"[a-zA-Z0-9_ ]*\"', current_line_region.begin())

            if class_region and class_region.contains(current_point):
                return COMPLETIONS
