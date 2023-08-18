from enum import Enum
import logging

_logger = logging.getLogger(__name__)

def create_config_arg_msg(arg_msg, arg_name, arg_value):
        """Creates a config protobuf message with the config argument name and value"""
        # Do not access enum value if it's the argument is not an enum
        setattr(
            arg_msg, arg_name, arg_value if not isinstance(arg_value,Enum) else \
            arg_value.value
        )
        return arg_msg

def create_config_request_from_args(config_msg, arg_msg, config_args_dict):
    """Creates a config message request with a given config argument dictionary"""
    # Create the set_config request message (Message with repeated arguments)
    # Append each config argument message to the config message
    for arg_name,arg_value in config_args_dict.items():
        request_argument = create_config_arg_msg(arg_msg,arg_name,arg_value)
        _logger.debug("Config argument message: %s", request_argument)
        config_msg.conf_arg.append(request_argument)

    return config_msg

def filter_arg_values(dictionary, filter_key, filter_value):
    """
    Gets a dictionary of arguments and filters unwanted keys by key or value. Returns a new
    dictionary
    """
    filtered_args_list = {
        key:value for (key,value) in dictionary.items()
                        if key != filter_key and value != filter_value
    }
    return filtered_args_list
