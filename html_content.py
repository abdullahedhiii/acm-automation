def get_html_content(template_path, params):
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Replace placeholders with actual values
    html_content = template.format(name=params["name"])

    return html_content

