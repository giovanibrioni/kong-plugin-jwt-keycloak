local plugin_name = "jwt-keycloak"
local package_name = "kong-plugin-" .. plugin_name
local package_version = "1.3.0"
local rockspec_revision = "1"

local github_account_name = "telekom-digioss"
local github_repo_name = package_name
local git_checkout = package_version == "dev" and "master" or package_version


package = package_name
version = package_version .. "-" .. rockspec_revision
supported_platforms = { "linux", "macosx" }
source = {
  url = "git+https://github.com/"..github_account_name.."/"..github_repo_name..".git",
  branch = git_checkout,
}


description = {
  summary = "A Kong plugin that will validate tokens issued by keycloak",
  homepage = "https://"..github_account_name..".github.io/"..github_repo_name,
  license = "Apache 2.0",
}


dependencies = {
  "lua ~> 5"
}


build = {
  type = "builtin",
  modules = {
    -- TODO: add any additional code files added to the plugin
    ["kong.plugins."..plugin_name..".handler"]            = "kong/plugins/jwt-keycloak/handler.lua",
    ["kong.plugins."..plugin_name..".schema"]             = "kong/plugins/jwt-keycloak/schema.lua",
    ["kong.plugins."..plugin_name..".keycloak_keys"]      = "kong/plugins/jwt-keycloak/keycloak_keys.lua",
    ["kong.plugins."..plugin_name..".key_conversion"]     = "kong/plugins/jwt-keycloak/key_conversion.lua",
    ["kong.plugins."..plugin_name..".validators.issuers"] = "kong/plugins/jwt-keycloak/validators/issuers.lua",
    ["kong.plugins."..plugin_name..".validators.roles"]   = "kong/plugins/jwt-keycloak/validators/roles.lua",
    ["kong.plugins."..plugin_name..".validators.scope"]   = "kong/plugins/jwt-keycloak/validators/scope.lua",
  }
}
