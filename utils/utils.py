import os


def create_experiment(time):
    """
    This function allows yout to create
    your experiment folder

    :param time:    timestamp value
    :type time:     str
    :param paths:   current path of the 
                    project
    :type paths:    dict
    """
    # Update experiment path
    paths['experiment'] = os.path.join(
        paths['results'], 
        time
    )

    # Create experiment directory
    os.mkdir(paths)

    # Update paths
    for key in paths['experiment_subfolder']:
        paths[key] = os.path.join(
            paths['results'], 
            paths[key]
        )
        # Create result subdirectories
        os.mkdir(paths[key])
        
