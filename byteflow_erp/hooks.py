app_name = "byteflow_erp"
app_title = "Byteflow ERP"
app_publisher = "Byteflow"
app_description = "Custom ERP solution for Kenya."
app_email = "byteflow@example.com"
app_license = "mit"
app_logo_url = "/assets/byteflow_erp/images/logo.png"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "byteflow_erp",
# 		"logo": "/assets/byteflow_erp/images/logo.png",
# 		"title": "Byteflow ERP",
# 		"route": "/byteflow_erp",
# 		"has_permission": "byteflow_erp.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/byteflow_erp/css/byteflow_erp.css"
# app_include_js = "/assets/byteflow_erp/js/byteflow_erp.js"

# include js, css files in header of web template
# web_include_css = "/assets/byteflow_erp/css/byteflow_erp.css"
# web_include_js = "/assets/byteflow_erp/js/byteflow_erp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "byteflow_erp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# include js in doctype views
doctype_js = {
    "Sales Invoice": "public/js/smart_download.js",
    "Purchase Order": "public/js/smart_download.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "byteflow_erp/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

website_context = {
	"favicon": "/assets/byteflow_erp/images/logo.png",
	"splash_image": "/assets/byteflow_erp/images/logo.png",
	"app_name": "Byteflow ERP",
    "app_logo": "/assets/byteflow_erp/images/logo.png",
}

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "byteflow_erp.utils.jinja_methods",
# 	"filters": "byteflow_erp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "byteflow_erp.install.before_install"
# after_install = "byteflow_erp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "byteflow_erp.uninstall.before_uninstall"
# after_uninstall = "byteflow_erp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "byteflow_erp.utils.before_app_install"
# after_app_install = "byteflow_erp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "byteflow_erp.utils.before_app_uninstall"
# after_app_uninstall = "byteflow_erp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "byteflow_erp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Payment Entry": {
		"on_submit": "byteflow_erp.mpesa.on_submit_payment_entry"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"byteflow_erp.tasks.all"
# 	],
# 	"daily": [
# 		"byteflow_erp.tasks.daily"
# 	],
# 	"hourly": [
# 		"byteflow_erp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"byteflow_erp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"byteflow_erp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "byteflow_erp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "byteflow_erp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "byteflow_erp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["byteflow_erp.utils.before_request"]
# after_request = ["byteflow_erp.utils.after_request"]

# Job Events
# ----------
# before_job = ["byteflow_erp.utils.before_job"]
# after_job = ["byteflow_erp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"byteflow_erp.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

