
output "hub_vnet_name" {
  value = azurerm_virtual_network.hub.name
}

output "app_vnet_name" {
  value = azurerm_virtual_network.spoke_app.name
}

output "storage_account_name" {
  value = azurerm_storage_account.tfstate.name
}