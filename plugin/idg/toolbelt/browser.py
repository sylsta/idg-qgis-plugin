from qgis.core import QgsDataItemProvider, QgsDataCollectionItem, QgsDataProvider
from qgis.PyQt.QtGui import QIcon
from idg.toolbelt import PluginGlobals 
from qgis.PyQt.QtWidgets import QAction, QMenu

class IdgProvider(QgsDataItemProvider):
    def __init__(self):
        QgsDataItemProvider.__init__(self)

    def name(self):
        return "IDG Provider"

    def capabilities(self):
        return QgsDataProvider.Net

    def createDataItem(self, path, parentItem):
        root = RootCollection()
        return root
  
        
class RootCollection(QgsDataCollectionItem):
    def __init__(self):
        QgsDataCollectionItem.__init__(self, None, "IDG", "/IDG")
        self.setIcon(QIcon(PluginGlobals.instance().plugin_path+'/resources/images/snowman-face-svgrepo-com.svg'))
        
    def actions(self, parent):
        actions = list()
        add_idg_action = QAction(QIcon(), 'Paramètres...', parent)
        
        actions.append(add_idg_action)
        return actions
        
    def menus(self, parent):
        menu = QMenu(title='Plateformes', parent=parent)
        for pf, checked in zip(['DataGrandEst', 'GeoBretagne', 'Geo2France', 'Indigeo'], [True, False, True, False]): # pour maquette TODO boucler sur une variable de conf
            action = QAction(pf, menu, checkable=True)
            action.setChecked(checked)
            menu.addAction(action) # TODO l'action permet d'activer/désactiver une plateforme. La désactivation supprime le DataCollectionItem et désactive le download du fichier de conf
        menu.addSeparator()
        menu.addAction(QAction('Ajouter une URL...', menu, )) # TODO Liens vers le panneau Options de QGIS
        return [menu]
        
    def createChildren(self):
        # TODO ajouter ici les DataCollectionItem des différentes plateformes
        return []
