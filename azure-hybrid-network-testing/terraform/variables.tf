
variable "location" {
  default = "East US"
}

variable "resource_group_name" {
  default = "rg-hybrid-network-testing"
}

variable "hub_vnet_cidr" {
  default = "10.0.0.0/16"
}

variable "spoke_app_cidr" {
  default = "10.1.0.0/16"
}

variable "spoke_db_cidr" {
  default = "10.2.0.0/16"
}

variable "firewall_private_ip" {
  default = "10.0.1.4"
}

variable "vpn_gateway_sku" {
  default = "VpnGw1"
}

variable "storage_account_name" {
  default = "sthybridtesting001"
}