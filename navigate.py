def navigate_to(target):
    """
    Simulates navigation path planning. Returns waypoints and ETA estimate.
    Replace with ROS, SLAM, or real path planning later.
    """
    if target == "harbor":
        return {"waypoints": [(0,0),(10,5),(20,10)], "eta_min": 12}
    if target == "hotspot":
        return {"waypoints": [(0,0),(5,4),(9,9)], "eta_min": 7}
    return {"waypoints": [(0,0)], "eta_min": 1}
