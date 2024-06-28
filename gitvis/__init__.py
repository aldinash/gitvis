__app_name__ = "gitvis"

(SUCCESS, DIR_ERROR, EMAIL_ERROR, DIR_ERROR, DATE_ERROR) = range(5)

ERRORS = {
    DIR_ERROR: "Please provide correct directory.",
    EMAIL_ERROR: "Cannot find global email. Try to pass email manually.",
    DATE_ERROR: "Date Error. Make sure your provided a valid date.",
}
