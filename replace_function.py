def create_transform_func(remove_index):
    def my_transform_func(inputs: dict):
        return transform_func(inputs, remove_index)
    return my_transform_func


def transform_func(inputs: dict, remove_index = 5) -> dict:
    text = inputs['input'].strip()
    accumulate = ""
    for i, s in enumerate(text.split(' ')):
        i = i + 1
        if i % remove_index != 0:
            accumulate += f"{s} "
    return {"input": accumulate.strip()}


if __name__ == '__main__':
    text = """
Minimum 5 years' experience in static website development (WordPress templating, PHP, HTML5, CSS3, Bootstrap, jQuery, MySQL, XML/JSON, cross-device and cross-browser development) and web app development (Angular or React, API integration, TDD, performance tuning, security).
    """
    my_func = create_transform_func(3)
    result_dict = my_func({'text': text})
    print(result_dict['input'])