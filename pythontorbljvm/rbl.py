# -*- coding: utf-8 -*-
"""
Python binding, via PyJnius, to RBL-JVM.

"""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Rbl(object):
    __metaclass__ = Singleton
    def __init__(self, **kwargs):
        self.root = kwargs['root']
        self.version = kwargs['version']
        import jnius_config
        jnius_config.add_options('-Xmx2g')
        jnius_config.set_classpath('{0}/lib/btrbl-je-{1}.jar'.format(self.root, self.version),
                                   '{0}/lib/slf4j-api-1.7.5.jar'.format(self.root),
                                   '{0}/lib/slf4j-simple-1.7.5.jar'.format(self.root))
        from jnius import autoclass
        self.BaseLinguisticsFactory = autoclass('com.basistech.rosette.bl.BaseLinguisticsFactory')
        self.Annotator = autoclass('com.basistech.rosette.dm.Annotator')
        self.BaseLinguisticsOption = autoclass('com.basistech.rosette.bl.BaseLinguisticsOption')
        self.EnumMap = autoclass('java.util.EnumMap')
        self.String = autoclass('java.lang.String')

    def factory(self):
        factory = self.BaseLinguisticsFactory()
        factory.setOption(self.BaseLinguisticsOption.rootDirectory, self.root)
        return factory

    def annotator(self, factory, **kwargs):
        optionMap = self.EnumMap(self.BaseLinguisticsOption)
        optionMap.put(self.BaseLinguisticsOption.language, kwargs['language'])
        return factory.createSingleLanguageAnnotator(optionMap)

    def charsequence(self, s):
        from jnius import cast
        return cast('java.lang.CharSequence', self.String(s))





