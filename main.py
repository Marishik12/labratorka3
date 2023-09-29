# import logging
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning4435346")
# logging.error("error")
# logging.critical("critical")

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     filename="logs.log",
#                     filemode="w")
# logging.debug("debug")
# logging.info("info")

# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     filename="logs.log",
#                     filemode="w",
#                     format="We have next logging "
#                            "message:%(asctime)s:%(levelname)"
#                            "s - %(message)s")
# logging.debug("debug")
# logging.info("info")

# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     filename="logs.log",
#                     filemode="w",
#                     format="We have next logging message: "
#                            "%(asctime)s : %(levelname)"
#                            "s -%(message)s")
# try:
#     print(10 / 0)
# except Exception:
#     logging.exception("Exception")

# if 2+2==4:
#     print("In fact, 2+2=4")

# assert 2+2==5

# assert 2+2==5,"Wrong assert"

# """
# >>> 2+2
# 5
# """
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

# def adder (*args, **kwargs):
#     result = 0
#     for _ in args:
#         result += _
#     for _ in kwargs.values():
#         result += _
#     return result
