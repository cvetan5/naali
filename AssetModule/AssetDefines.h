// For conditions of distribution and use, see copyright notice in license.txt

#ifndef incl_Asset_AssetDefines_h
#define incl_Asset_AssetDefines_h

namespace Asset
{
    // Asset types
    const Core::asset_type_t RexAT_Texture = 0;
    
    // Asset channels
    const int RexAC_Unknown = 0;
    const int RexAC_Miscellaneous = 1;
    const int RexAC_Asset = 2;
    
    // Asset sources
    const int RexAS_Unknown = 0;
    const int RexAS_Asset = 2;
    const int RexAS_Inventory = 3;
    
    // Image types
    const int RexIT_Normal = 0;
    
    // Asset transfer status codes
    const int RexTS_Ok = 0;
    const int RexTS_Done = 1;
    const int RexTS_Skip = 2;
    const int RexTS_Abort = 3;
    const int RexTS_Error = -1;
    const int RexTS_UnknownSource = -2;
    const int RexTS_NoPermission = -3;
    const int RexTS_UnknownError = -4;
}

#endif