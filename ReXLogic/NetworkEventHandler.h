// For conditions of distribution and use, see copyright notice in license.txt

#ifndef incl_NetworkEventHandler_h
#define incl_NetworkEventHandler_h

#include "ComponentInterface.h"
#include "Foundation.h"
#include "NetworkEvents.h"

namespace OpenSimProtocol
{
    class OpenSimProtocolModule;
}

namespace RexLogic
{
    struct DecodedTerrainPatch;
    class RexLogicModule;

    /// Handles incoming SLUDP network events in a Rex-specific way. \todo Break down into more logical functions.
    class NetworkEventHandler
    {
    public:
        NetworkEventHandler(Foundation::Framework *framework, RexLogicModule *rexlogicmodule);
        virtual ~NetworkEventHandler();

        // !Handle network events coming from OpenSimProtocolModule
        bool HandleOpenSimNetworkEvent(Core::event_id_t event_id, Foundation::EventDataInterface* data);
    private:
        // !Handler functions for Opensim network events
        bool HandleOSNE_AgentMovementComplete(OpenSimProtocol::NetworkEventInboundData* data);
        bool HandleOSNE_GenericMessage(OpenSimProtocol::NetworkEventInboundData* data);
        bool HandleOSNE_ImprovedTerseObjectUpdate(OpenSimProtocol::NetworkEventInboundData* data);
        bool HandleOSNE_KillObject(OpenSimProtocol::NetworkEventInboundData* data);
        bool HandleOSNE_LogoutReply(OpenSimProtocol::NetworkEventInboundData* data);
        bool HandleOSNE_ObjectUpdate(OpenSimProtocol::NetworkEventInboundData* data);
        bool HandleOSNE_ObjectProperties(OpenSimProtocol::NetworkEventInboundData* data);
        bool HandleOSNE_RegionHandshake(OpenSimProtocol::NetworkEventInboundData* data);

        //! Handler functions for GenericMessages
        bool HandleRexGM_RexMediaUrl(OpenSimProtocol::NetworkEventInboundData* data);
        bool HandleRexGM_RexPrimData(OpenSimProtocol::NetworkEventInboundData* data);
        bool HandleRexGM_RexAppearance(OpenSimProtocol::NetworkEventInboundData* data);

        //! Handler functions for terseobjectupdates
        void HandleTerseObjectUpdate_30bytes(const uint8_t* bytes);
        void HandleTerseObjectUpdateForPrim_60bytes(const uint8_t* bytes);
        void HandleTerseObjectUpdateForAvatar_60bytes(const uint8_t* bytes);



        //! @return The entity corresponding to given id AND uuid. This entity is guaranteed to have an existing EC_OpenSimPrim component.
        //!         Does not return null. If the entity doesn't exist, an entity with the given entityid and fullid is created and returned.
        Foundation::EntityPtr GetOrCreatePrimEntity(Core::entity_id_t entityid, const RexUUID &fullid);
        Foundation::EntityPtr CreateNewPrimEntity(Core::entity_id_t entityid);



        //! @return The entity corresponding to given id AND uuid. This entity is guaranteed to have an existing EC_OpenSimAvatar component.
        //!         Does not return null. If the entity doesn't exist, an entity with the given entityid and fullid is created and returned.
        Foundation::EntityPtr GetOrCreateAvatarEntity(Core::entity_id_t entityid, const RexUUID &fullid);
        Foundation::EntityPtr CreateNewAvatarEntity(Core::entity_id_t entityid);

        //! Creates an OBB for debug visualization of the extents of the given scene object.
        void DebugCreateOgreBoundingBox(const Foundation::ComponentInterfacePtr ogrePlaceable, const std::string &materialName);

        void DebugCreateTerrainVisData(const DecodedTerrainPatch &heightData, int patchSize);

        //! Helper functions for getting values from terseupdate packets
        Core::Quaternion GetProcessedQuaternion(const uint8_t* bytes);
        Core::Vector3df GetProcessedScaledVectorFromUint16(const uint8_t* bytes, float scale);
        Core::Vector3df GetProcessedVectorFromUint16(const uint8_t* bytes);
        Core::Vector3df GetProcessedVector(const uint8_t* bytes);

        Foundation::Framework *framework_;
        OpenSimProtocol::OpenSimProtocolModule *netInterface_;
        
        RexLogicModule *rexlogicmodule_;
    };
}

#endif
