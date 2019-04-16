"""PyTest Fixtures"""

import pytest
from pyodata.v2.model import Edmx


@pytest.fixture
def metadata():
    """Example OData metadata"""

    # pylint: disable=line-too-long

    return """<edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns:sap="http://www.sap.com/Protocols/SAPData" Version="1.0">
          <edmx:Reference xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx" Uri="https://example.sap.corp/sap/opu/odata/IWFND/CATALOGSERVICE;v=2/Vocabularies(TechnicalName='%2FIWBEP%2FVOC_COMMON',Version='0001',SAP__Origin='LOCAL')/$value">
           <edmx:Include Namespace="com.sap.vocabularies.Common.v1" Alias="Common"/>
          </edmx:Reference>
         <edmx:DataServices m:DataServiceVersion="2.0">
          <Schema xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://schemas.microsoft.com/ado/2008/09/edm" Namespace="EXAMPLE_SRV" xml:lang="en" sap:schema-version="1">
           <EntityType Name="MasterEntity" sap:content-version="1">
            <Key><PropertyRef Name="Key"/></Key>
            <Property Name="Key" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Key" sap:creatable="false" sap:updatable="false" sap:sortable="false" sap:value-list="standard"/>
            <Property Name="DataType" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Key" sap:creatable="false" sap:updatable="false" sap:sortable="false"/>
            <Property Name="Data" Type="Edm.String" MaxLength="Max" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="false" sap:filterable="false" sap:text="DataName"/>
            <Property Name="DataName" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="false" sap:filterable="false"/>
           </EntityType>
           <EntityType Name="DataEntity" sap:content-version="1" sap:value-list="true" sap:label="Data entities">
            <Key><PropertyRef Name="Name"/></Key>
            <Property Name="Name" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="false" sap:filterable="false"/>
            <Property Name="Type" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="false" sap:filterable="false"/>
            <Property Name="Value" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="false" sap:filterable="false"/>
            <Property Name="Description" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="false" sap:filterable="false"/>
            <Property Name="Invisible" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="false" sap:filterable="false" sap:visible="false"/>
           </EntityType>
           <EntityType Name="AnnotationTest" sap:content-version="1" sap:label="Annotations Tests">
            <Key><PropertyRef Name="NoFormat"/></Key>
            <Property Name="NoFormat" Type="Edm.String"/>
            <Property Name="UpperCase" Type="Edm.String" sap:display-format="UpperCase"/>
            <Property Name="Date" Type="Edm.DateTime" sap:display-format="Date"/>
            <Property Name="NonNegative" Type="Edm.Decimal" sap:display-format="NonNegative"/>
           </EntityType>
           <EntityType Name="TemperatureMeasurement" sap:content-version="1" sap:value-list="true" sap:label="Data entities">
            <Key>
              <PropertyRef Name="Sensor"/>
              <PropertyRef Name="Date"/>
            </Key>
            <Property Name="Sensor" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="true" sap:filterable="true"/>
            <Property Name="Date" Type="Edm.DateTime" Nullable="false"  sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="true" sap:filterable="true"/>
            <Property Name="Value" Type="Edm.Double" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="true" sap:filterable="true"/>
           </EntityType>
           <EntityType Name="City" sap:content-version="1" sap:value-list="true" sap:label="City">
            <Key>
              <PropertyRef Name="Name"/>
              <PropertyRef Name="CountryISO"/>
            </Key>
            <Property Name="Name" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="true" sap:filterable="true"/>
            <Property Name="CountryISO" Type="Edm.String" Nullable="false"  sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="true" sap:filterable="true"/>
            <Property Name="Country" Type="Edm.String" Nullable="false"  sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="true" sap:filterable="true"/>
           </EntityType>
           <EntityType Name="Car" sap:content-version="1" sap:value-list="true" sap:label="Car">
            <Key>
              <PropertyRef Name="Name"/>
            </Key>
            <Property Name="Name" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="true" sap:filterable="true"/>
            <Property Name="CodeName" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="true" sap:filterable="true" sap:filter-restriction="single-value" sap:required-in-filter="true"/>
            <Property Name="Price" Type="Edm.Decimal" Nullable="false" Precision="7" Scale="3" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="true" sap:filterable="true"/>
            <NavigationProperty Name="IDPic" Relationship="EXAMPLE_SRV.toCarIDPic" FromRole="FromRole_toCarIDPic" ToRole="ToRole_toCarIDPic"/>
           </EntityType>
           <EntityType Name="CarIDPic" m:HasStream="true" sap:content-versiom="1" sap:label="Car ID">
            <Key>
             <PropertyRef Name="CarName"/>
            </Key>
            <Property Name="CarName" Type="Edm.String" Nullable="false" sap:unicode="false" sap:label="Data" sap:creatable="false" sap:updatable="false" sap:sortable="true" sap:filterable="true"/>
            <Property Name="Content" Type="Edm.Binary" Nullable="false" sap:label="Picture" sap:creatable="false" sap:updatable="false" sap:sortable="false" sap:filterable="false"/>
           </EntityType>

           <EntityType Name="Customer">
            <Key>
             <PropertyRef Name="Name"/>
            </Key>
            <Property Name="Name" Type="Edm.String" Nullable="false" />
            <NavigationProperty Name="Orders" Relationship="EXAMPLE_SRV.CustomerOrders" FromRole="CustomerRole" ToRole="OrdersRole"/>
           </EntityType>

           <EntityType Name="Order">
            <Key>
             <PropertyRef Name="Number"/>
            </Key>
            <Property Name="Number" Type="Edm.String" Nullable="false" />
            <Property Name="Owner" Type="Edm.String" Nullable="false" />
           </EntityType>

           <ComplexType Name="ComplexNumber">
            <Property Name="Real" Type="Edm.Double" Nullable="false"/>
            <Property Name="Imaginary" Type="Edm.Double" Nullable="false"/>
           </ComplexType>
           <ComplexType Name="Rectangle">
            <Property Name="Width" Type="Edm.Double" Nullable="false"/>
            <Property Name="Height" Type="Edm.Double" Nullable="false"/>
           </ComplexType>
           <ComplexType Name="Building">
             <Property Name="Street" Type="Edm.String" Nullable="true"/>
             <Property Name="Number" Type="Edm.String" Nullable="false"/>
             <Property Name="City" Type="Edm.String" Nullable="false"/>
             <Property Name="Region" Type="Edm.String" Nullable="false"/>
             <Property Name="Country" Type="Edm.String" Nullable="false"/>
           </ComplexType>
           <Association Name="toDataEntity" sap:content-version="1">
            <End Type="EXAMPLE_SRV.MasterEntity" Multiplicity="1" Role="FromRole_toDataEntity" />
            <End Type="EXAMPLE_SRV.DataEntity" Multiplicity="*" Role="ToRole_toDataEntity" />
            <ReferentialConstraint>
             <Principal Role="FromRole_toDataEntity">
              <PropertyRef Name="Key" />
             </Principal>
             <Dependent Role="ToRole_toDataEntity">
              <PropertyRef Name="Name" />
             </Dependent>
            </ReferentialConstraint>
           </Association>
           <Association Name="toCarIDPic" sap:content-version="1">
            <End Type="EXAMPLE_SRV.Car" Multiplicity="1" Role="FromRole_toCarIDPic" />
            <End Type="EXAMPLE_SRV.CarIDPic" Multiplicity="1" Role="ToRole_toCarIDPic" />
            <ReferentialConstraint>
             <Principal Role="FromRole_toCarIDPic">
              <PropertyRef Name="Name" />
             </Principal>
             <Dependent Role="ToRole_toCarIDPic">
              <PropertyRef Name="CarName" />
             </Dependent>
            </ReferentialConstraint>
           </Association>

           <Association Name="CustomerOrders">
            <End Role="CustomerRole" Type="EXAMPLE_SRV.Customer" Multiplicity="1"/>
            <End Role="OrdersRole" Type="EXAMPLE_SRV.Order" Multiplicity="*"/>
            <ReferentialConstraint>
             <Principal Role="CustomerRole">
              <PropertyRef Name="Name"/>
             </Principal>
             <Dependent Role="OrdersRole">
              <PropertyRef Name="Owner"/>
             </Dependent>
            </ReferentialConstraint>
           </Association>

           <EntityContainer Name="EXAMPLE_SRV" m:IsDefaultEntityContainer="true" sap:supported-formats="atom json xlsx">
            <EntitySet Name="MasterEntities" EntityType="EXAMPLE_SRV.MasterEntity" sap:label="Master entities" sap:creatable="false" sap:updatable="false" sap:deletable="false" sap:searchable="true" sap:content-version="1"/>
            <EntitySet Name="DataValueHelp" EntityType="EXAMPLE_SRV.DataEntity" sap:creatable="false" sap:updatable="false" sap:deletable="false" sap:searchable="true" sap:content-version="1"/>
            <EntitySet Name="Cities" EntityType="EXAMPLE_SRV.City" sap:creatable="false" sap:updatable="false" sap:deletable="false" sap:searchable="true" sap:content-version="1"/>
            <EntitySet Name="CitiesWithFilter" EntityType="EXAMPLE_SRV.City" sap:requires-filter="true"/>
            <EntitySet Name="CitiesNotAddressable" EntityType="EXAMPLE_SRV.City" sap:addressable="false"/>
            <EntitySet Name="Cars" EntityType="EXAMPLE_SRV.Car" sap:countable="false" sap:pageable="false" sap:topable="true"/>
            <EntitySet Name="CarIDPics" EntityType="EXAMPLE_SRV.CarIDPic" sap:countable="false" sap:pageable="false" sap:topable="false"/>
            <FunctionImport Name="retrieve" ReturnType="Edm.Boolean" EntitySet="MasterEntities" m:HttpMethod="GET" sap:action-for="EXAMPLE_SRV.MasterEntity">
             <Parameter Name="Param" Type="Edm.String" Mode="In" MaxLenght="5" />
            </FunctionImport>
            <AssociationSet Name="toDataEntitySet" Association="EXAMPLE_SRV.toDataEntity" sap:creatable="false" sap:updatable="false" sap:deletable="false" sap:content-version="1">
                <End EntitySet="MasterEntities" Role="FromRole_toDataEntity" />
                <End EntitySet="DataValueHelp" Role="ToRole_toDataEntity" />
            </AssociationSet>
            <AssociationSet Name="toCarIDPicSet" Association="EXAMPLE_SRV.toCarIDPic" sap:creatable="false" sap:updatable="false" sap:deletable="false" sap:content-version="1">
              <End EntitySet="Cars" Role="FromRole_toCarIDPic" />
              <End EntitySet="CarIDPics" Role="ToRole_toCarIDPic" />
            </AssociationSet>
           </EntityContainer>
           <Annotations xmlns="http://docs.oasis-open.org/odata/ns/edm" Target="EXAMPLE_SRV.MasterEntity/Data">
            <Annotation Term="com.sap.vocabularies.Common.v1.ValueList">
             <Record>
              <PropertyValue Property="Label" String="Data"/>
              <PropertyValue Property="CollectionPath" String="DataValueHelp"/>
              <PropertyValue Property="SearchSupported" Bool="true"/>
              <PropertyValue Property="Parameters">
               <Collection>
                <Record Type="com.sap.vocabularies.Common.v1.ValueListParameterIn">
                 <PropertyValue Property="LocalDataProperty" PropertyPath="DataType"/>
                 <PropertyValue Property="ValueListProperty" String="Type"/>
                </Record>
                <Record Type="com.sap.vocabularies.Common.v1.ValueListParameterOut">
                 <PropertyValue Property="LocalDataProperty" PropertyPath="Data"/>
                 <PropertyValue Property="ValueListProperty" String="Value"/>
                </Record>
                <Record Type="com.sap.vocabularies.Common.v1.ValueListParameterInOut">
                 <PropertyValue Property="LocalDataProperty" PropertyPath="DataName"/>
                 <PropertyValue Property="ValueListProperty" String="Name"/>
                </Record>
                <Record Type="com.sap.vocabularies.Common.v1.ValueListParameterDisplayOnly">
                 <PropertyValue Property="ValueListProperty" String="Description"/>
                </Record>
               </Collection>
              </PropertyValue>
             </Record>
            </Annotation>
           </Annotations>
           <Annotations xmlns="http://docs.oasis-open.org/odata/ns/edm" Target="EXAMPLE_SRV.Building/City">
            <Annotation Term="Common.ValueList">
             <Record>
              <PropertyValue Property="Label" String="Name"/>
              <PropertyValue Property="CollectionPath" String="Cities"/>
              <PropertyValue Property="SearchSupported" Bool="true"/>
              <PropertyValue Property="Parameters">
               <Collection>
                <Record Type="Common.ValueListParameterInOut">
                 <PropertyValue Property="LocalDataProperty" PropertyPath="City"/>
                 <PropertyValue Property="ValueListProperty" String="Name"/>
                </Record>
                <Record Type="Common.ValueListParameterDisplayOnly">
                 <PropertyValue Property="ValueListProperty" String="Country"/>
                </Record>
               </Collection>
              </PropertyValue>
             </Record>
            </Annotation>
           </Annotations>
           <Annotations xmlns="http://docs.oasis-open.org/odata/ns/edm" Target="EXAMPLE_SRV.Building/City" Qualifier="2ND_BUILDING_CITY_IGNORED">
            <Annotation Term="com.sap.vocabularies.Common.v1.ValueList">
             <Record>
              <PropertyValue Property="Label" String="Name"/>
              <PropertyValue Property="CollectionPath" String="Cities"/>
              <PropertyValue Property="SearchSupported" Bool="true"/>
              <PropertyValue Property="Parameters">
               <Collection>
                <Record Type="com.sap.vocabularies.Common.v1.ValueListParameterInOut">
                 <PropertyValue Property="LocalDataProperty" PropertyPath="City"/>
                 <PropertyValue Property="ValueListProperty" String="Name"/>
                </Record>
               </Collection>
              </PropertyValue>
             </Record>
            </Annotation>
           </Annotations>
          </Schema>

          <Schema xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://schemas.microsoft.com/ado/2008/09/edm" Namespace="EXAMPLE_SRV_SETS" xml:lang="en" sap:schema-version="1">

            <EntityType Name="Employee">
                <Key>
                    <PropertyRef Name="ID"/>
                </Key>
                <Property Name="ID" Type="Edm.Int32" Nullable="false"/>
                <Property Name="NameFirst" Type="Edm.String" Nullable="true"/>
                <Property Name="NameLast" Type="Edm.String" Nullable="true"/>
                <NavigationProperty Name="Addresses" Relationship="EXAMPLE_SRV_SETS.AssociationEmployeeAddress" FromRole="EmployeeRole" ToRole="AddressRole"/>
            </EntityType>

            <EntityType Name="Address">
                <Key>
                    <PropertyRef Name="ID"/>
                </Key>
                <Property Name="ID" Type="Edm.Int32" Nullable="false"/>
                <Property Name="Street" Type="Edm.String" Nullable="true"/>
                <Property Name="City" Type="Edm.String" Nullable="true"/>
            </EntityType>

            <Association Name="AssociationEmployeeAddress">
                <End Type="EXAMPLE_SRV_SETS.Employee" Multiplicity="1" Role="EmployeeRole"/>
                <End Type="EXAMPLE_SRV_SETS.Address" Multiplicity="*" Role="AddressRole"/>
            </Association>

            <ComplexType Name="Rectangle">
                <Property Name="Width" Type="Edm.Double" Nullable="false"/>
                <Property Name="Height" Type="Edm.Double" Nullable="false"/>
            </ComplexType>

            <EntityContainer Name="EXAMPLE_SRV" m:IsDefaultEntityContainer="true" sap:supported-formats="atom json xlsx">

                <EntitySet Name="TemperatureMeasurements" EntityType="EXAMPLE_SRV.TemperatureMeasurement" sap:creatable="true" sap:updatable="true" sap:deletable="true" sap:searchable="true" sap:content-version="1"/>

                <EntitySet Name="Employees" EntityType="Employee"/>

                <EntitySet Name="Addresses" EntityType="Address"/>

                <EntitySet Name="Customers" EntityType="EXAMPLE_SRV.Customer"/>

                <EntitySet Name="Orders" EntityType="EXAMPLE_SRV.Order"/>

                <FunctionImport Name="get_max" ReturnType="TemperatureMeasurement" EntitySet="TemperatureMeasurements" m:HttpMethod="GET" />

                <FunctionImport Name="get_best_measurements" ReturnType="Collection(EXAMPLE_SRV.TemperatureMeasurement)" EntitySet="EXAMPLE_SRV.TemperatureMeasurements" m:HttpMethod="GET" />

                <FunctionImport Name="sum" ReturnType="Edm.Int32" m:HttpMethod="GET">
                    <Parameter Name="A" Type="Edm.Int32" Mode="In" />
                    <Parameter Name="B" Type="Edm.Int32" Mode="In" />
                </FunctionImport>

                <FunctionImport Name="sum_complex" ReturnType="EXAMPLE_SRV.ComplexNumber" m:HttpMethod="GET">
                    <Parameter Name="Param" Type="EXAMPLE_SRV.ComplexNumber" Mode="In" />
                    <Parameter Name="Param" Type="EXAMPLE_SRV.ComplexNumber" Mode="In" />
                </FunctionImport>

                <AssociationSet Name="AssociationEmployeeAddress_AssocSet" Association="EXAMPLE_SRV_SETS.AssociationEmployeeAddress" sap:creatable="false" sap:updatable="false" sap:deletable="false" sap:content-version="1">
                    <End Role="EmployeeRole" EntitySet="Employees"/>
                    <End Role="AddressRole" EntitySet="Addresses"/>
                </AssociationSet>

                <AssociationSet Name="CustomerOrder_AssocSet" Association="EXAMPLE_SRV.CustomerOrders">
                    <End Role="CustomerRole" EntitySet="Customers"/>
                    <End Role="OrdersRole" EntitySet="Orders"/>
                </AssociationSet>

            </EntityContainer>

          </Schema>
         </edmx:DataServices>
         </edmx:Edmx>"""


@pytest.fixture
def metadata_builder_factory():
    """Skeleton OData metadata"""

    # pylint: disable=line-too-long

    class MetadaBuilder(object):
        """Helper class for building XML metadata document"""

        PROLOGUE = """
        <edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns:sap="http://www.sap.com/Protocols/SAPData" Version="1.0">
          <edmx:Reference xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx" Uri="https://example.sap.corp/sap/opu/odata/IWFND/CATALOGSERVICE;v=2/Vocabularies(TechnicalName='%2FIWBEP%2FVOC_COMMON',Version='0001',SAP__Origin='LOCAL')/$value">
           <edmx:Include Namespace="com.sap.vocabularies.Common.v1" Alias="Common"/>
          </edmx:Reference>
         <edmx:DataServices m:DataServiceVersion="2.0">
         """

        EPILOGUE = """
         </edmx:DataServices>
        </edmx:Edmx>
        """

        def __init__(self):
            self._schemas = ''

        def add_schema(self, namespace, xml_definition):
            """Add schema element"""

            self._schemas += '<Schema xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://schemas.microsoft.com/ado/2008/09/edm" Namespace="{0}" xml:lang="en" sap:schema-version="1">'.format(namespace)
            self._schemas += xml_definition
            self._schemas += '</Schema>'

        def serialize(self):
            """Returns full metadata XML document"""

            return MetadaBuilder.PROLOGUE + self._schemas + MetadaBuilder.EPILOGUE

    return MetadaBuilder


@pytest.fixture
def schema(metadata):
    """Parsed metadata"""

    # pylint: disable=redefined-outer-name

    return Edmx.parse(metadata)


@pytest.fixture
def metadata_api_oregonlegislature_gov():
    """Metadata from the issue #16"""

    return """<edmx:Edmx xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx" Version="1.0">
  <edmx:DataServices xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" m:DataServiceVersion="1.0" m:MaxDataServiceVersion="3.0">
    <Schema xmlns="http://schemas.microsoft.com/ado/2009/11/edm" Namespace="State.Or.Leg.API.OData">
      <EntityType Name="LegislativeSession">
        <Key>
          <PropertyRef Name="SessionKey"/>
        </Key>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="SessionName" Type="Edm.String" Nullable="false" MaxLength="30" FixedLength="false" Unicode="false"/>
        <Property Name="BeginDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="EndDate" Type="Edm.DateTime" Precision="3"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <Property Name="DefaultSession" Type="Edm.Boolean" Nullable="false"/>
        <NavigationProperty Name="Measures" Relationship="State.Or.Leg.API.OData.LegislativeSessionMeasure" ToRole="Measure" FromRole="LegislativeSession"/>
        <NavigationProperty Name="Committees" Relationship="State.Or.Leg.API.OData.LegislativeSessionCommittees" ToRole="Committees" FromRole="LegislativeSession"/>
        <NavigationProperty Name="Legislators" Relationship="State.Or.Leg.API.OData.LegislativeSessionLegislator" ToRole="Legislator" FromRole="LegislativeSession"/>
        <NavigationProperty Name="ConveneTimes" Relationship="State.Or.Leg.API.OData.LegislativeSessionConveneTime" ToRole="ConveneTime" FromRole="LegislativeSession"/>
        <NavigationProperty Name="FloorSessionAgendaItems" Relationship="State.Or.Leg.API.OData.LegislativeSessionFloorSessionAgendaItem" ToRole="FloorSessionAgendaItem" FromRole="LegislativeSession"/>
        <NavigationProperty Name="FloorLetters" Relationship="State.Or.Leg.API.OData.LegislativeSessionFloorLetter" ToRole="FloorLetter" FromRole="LegislativeSession"/>
        <NavigationProperty Name="CommitteeMembers" Relationship="State.Or.Leg.API.OData.LegislativeSessionCommitteeMember" ToRole="CommitteeMember" FromRole="LegislativeSession"/>
      </EntityType>
      <EntityType Name="Measure">
        <Key>
          <PropertyRef Name="MeasureNumber"/>
          <PropertyRef Name="MeasurePrefix"/>
          <PropertyRef Name="SessionKey"/>
        </Key>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="MeasurePrefix" Type="Edm.String" Nullable="false" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32" Nullable="false"/>
        <Property Name="CatchLine" Type="Edm.String" MaxLength="2000" FixedLength="false" Unicode="false"/>
        <Property Name="MinorityCatchLine" Type="Edm.String" MaxLength="2000" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureSummary" Type="Edm.String" MaxLength="4000" FixedLength="false" Unicode="false"/>
        <Property Name="CurrentVersion" Type="Edm.String" MaxLength="1" FixedLength="false" Unicode="false"/>
        <Property Name="RelatingToFull" Type="Edm.String" MaxLength="4000" FixedLength="false" Unicode="false"/>
        <Property Name="RelatingTo" Type="Edm.String" MaxLength="2000" FixedLength="false" Unicode="false"/>
        <Property Name="AtTheRequestOf" Type="Edm.String" MaxLength="1000" FixedLength="false" Unicode="false"/>
        <Property Name="ChapterNumber" Type="Edm.String" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="CurrentLocation" Type="Edm.String" Nullable="false" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="CurrentCommitteeCode" Type="Edm.String" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="CurrentSubCommittee" Type="Edm.String" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="FiscalImpact" Type="Edm.String" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="RevenueImpact" Type="Edm.String" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="EmergencyClause" Type="Edm.Boolean"/>
        <Property Name="EffectiveDate" Type="Edm.DateTime" Precision="3"/>
        <Property Name="FiscalAnalyst" Type="Edm.String" MaxLength="91" FixedLength="false" Unicode="false"/>
        <Property Name="RevenueEconomist" Type="Edm.String" MaxLength="91" FixedLength="false" Unicode="false"/>
        <Property Name="LCNumber" Type="Edm.Int32"/>
        <Property Name="Vetoed" Type="Edm.Boolean"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <Property Name="PrefixMeaning" Type="Edm.String" Nullable="false" MaxLength="250" FixedLength="false" Unicode="false"/>
        <NavigationProperty Name="LegislativeSession" Relationship="State.Or.Leg.API.OData.LegislativeSessionMeasure" ToRole="LegislativeSession" FromRole="Measure"/>
        <NavigationProperty Name="CommitteeAgendaItems" Relationship="State.Or.Leg.API.OData.MeasureCommitteeAgendaItem" ToRole="CommitteeAgendaItem" FromRole="Measure"/>
        <NavigationProperty Name="CommitteeMeetingDocuments" Relationship="State.Or.Leg.API.OData.MeasureCommitteeMeetingDocument" ToRole="CommitteeMeetingDocument" FromRole="Measure"/>
        <NavigationProperty Name="FloorSessionAgendaItems" Relationship="State.Or.Leg.API.OData.MeasureFloorSessionAgendaItem" ToRole="FloorSessionAgendaItem" FromRole="Measure"/>
        <NavigationProperty Name="MeasureDocuments" Relationship="State.Or.Leg.API.OData.MeasureMeasureDocument" ToRole="MeasureDocument" FromRole="Measure"/>
        <NavigationProperty Name="MeasureAnalysisDocuments" Relationship="State.Or.Leg.API.OData.MeasureMeasureAnalysisDocument" ToRole="MeasureAnalysisDocument" FromRole="Measure"/>
        <NavigationProperty Name="MeasureHistoryActions" Relationship="State.Or.Leg.API.OData.MeasureMeasureHistoryAction" ToRole="MeasureHistoryAction" FromRole="Measure"/>
        <NavigationProperty Name="MeasureSponsors" Relationship="State.Or.Leg.API.OData.MeasureMeasureSponsor" ToRole="MeasureSponsor" FromRole="Measure"/>
        <NavigationProperty Name="FloorLetters" Relationship="State.Or.Leg.API.OData.FloorLetterMeasure" ToRole="FloorLetter" FromRole="Measure"/>
        <NavigationProperty Name="MeasureVote" Relationship="State.Or.Leg.API.OData.MeasureMeasureVote" ToRole="MeasureVote" FromRole="Measure"/>
        <NavigationProperty Name="CommitteeVotes" Relationship="State.Or.Leg.API.OData.CommitteeVoteMeasure" ToRole="CommitteeVote" FromRole="Measure"/>
      </EntityType>
      <EntityType Name="Committee">
        <Key>
          <PropertyRef Name="CommitteeCode"/>
          <PropertyRef Name="SessionKey"/>
        </Key>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="CommitteeCode" Type="Edm.String" Nullable="false" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="CommitteeName" Type="Edm.String" Nullable="false" MaxLength="100" FixedLength="false" Unicode="false"/>
        <Property Name="HouseOfAction" Type="Edm.String" Nullable="false" MaxLength="1" FixedLength="false" Unicode="false"/>
        <Property Name="CommitteeType" Type="Edm.String" Nullable="false" MaxLength="100" FixedLength="false" Unicode="false"/>
        <Property Name="OfficeAddress" Type="Edm.String" MaxLength="5" FixedLength="false" Unicode="false"/>
        <Property Name="OfficePhone" Type="Edm.String" MaxLength="15" FixedLength="false" Unicode="false"/>
        <Property Name="FaxNumber" Type="Edm.String" MaxLength="15" FixedLength="false" Unicode="false"/>
        <Property Name="WebAddress" Type="Edm.String" MaxLength="100" FixedLength="false" Unicode="false"/>
        <Property Name="EmailAddress" Type="Edm.String" MaxLength="100" FixedLength="false" Unicode="false"/>
        <Property Name="ParentCommitteeCode" Type="Edm.String" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="LegislativeSession" Relationship="State.Or.Leg.API.OData.LegislativeSessionCommittees" ToRole="LegislativeSession" FromRole="Committees"/>
        <NavigationProperty Name="CommitteeMeetings" Relationship="State.Or.Leg.API.OData.CommitteesCommitteeMeetings" ToRole="CommitteeMeetings" FromRole="Committees"/>
        <NavigationProperty Name="ParentCommittee" Relationship="State.Or.Leg.API.OData.CommitteesParentCommittees" ToRole="Committees1" FromRole="Committees"/>
        <NavigationProperty Name="SubCommittees" Relationship="State.Or.Leg.API.OData.CommitteesParentCommittees" ToRole="Committees" FromRole="Committees1"/>
        <NavigationProperty Name="CommitteeStaffMembers" Relationship="State.Or.Leg.API.OData.CommitteeCommitteeStaff" ToRole="CommitteeStaff" FromRole="Committee"/>
        <NavigationProperty Name="MeasureAnalysisDocuments" Relationship="State.Or.Leg.API.OData.CommitteeMeasureAnalysisDocument" ToRole="MeasureAnalysisDocument" FromRole="Committee"/>
        <NavigationProperty Name="MeasureSponsors" Relationship="State.Or.Leg.API.OData.CommitteeMeasureSponsor" ToRole="MeasureSponsor" FromRole="Committee"/>
        <NavigationProperty Name="CommitteeMembers" Relationship="State.Or.Leg.API.OData.CommitteeCommitteeMember" ToRole="CommitteeMember" FromRole="Committee"/>
      </EntityType>
      <EntityType Name="CommitteeMeeting">
        <Key>
          <PropertyRef Name="CommitteeCode"/>
          <PropertyRef Name="MeetingDate"/>
          <PropertyRef Name="SessionKey"/>
        </Key>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="CommitteeCode" Type="Edm.String" Nullable="false" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="MeetingDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="Location" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="PostedDate" Type="Edm.DateTime" Precision="3"/>
        <Property Name="AlternateLocation" Type="Edm.String" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="AgendaUrl" Type="Edm.String" MaxLength="93" FixedLength="false" Unicode="false"/>
        <Property Name="AgendaRevisionNumber" Type="Edm.Int32" Nullable="false"/>
        <Property Name="MeetingStatusCode" Type="Edm.String" Nullable="false" MaxLength="1" FixedLength="false" Unicode="false"/>
        <Property Name="MeetingStatus" Type="Edm.String" Nullable="false" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="MeetingGuid" Type="Edm.Guid"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="Committee" Relationship="State.Or.Leg.API.OData.CommitteesCommitteeMeetings" ToRole="Committees" FromRole="CommitteeMeetings"/>
        <NavigationProperty Name="CommitteeAgendaItems" Relationship="State.Or.Leg.API.OData.CommitteeMeetingCommitteeAgendaItem" ToRole="CommitteeAgendaItem" FromRole="CommitteeMeeting"/>
        <NavigationProperty Name="CommitteeMeetingDocuments" Relationship="State.Or.Leg.API.OData.CommitteeMeetingCommitteeMeetingDocument" ToRole="CommitteeMeetingDocument" FromRole="CommitteeMeeting"/>
      </EntityType>
      <EntityType Name="CommitteeAgendaItem">
        <Key>
          <PropertyRef Name="CommitteeAgendaItemId"/>
        </Key>
        <Property Name="CommitteeAgendaItemId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="CommitteCode" Type="Edm.String" Nullable="false" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="MeetingDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="MeasurePrefix" Type="Edm.String" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32"/>
        <Property Name="BoardName" Type="Edm.String" MaxLength="100" FixedLength="false" Unicode="false"/>
        <Property Name="ExecutiveAppointee" Type="Edm.String" MaxLength="90" FixedLength="false" Unicode="false"/>
        <Property Name="MeetingType" Type="Edm.String" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="Action" Type="Edm.String" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="PrintOrder" Type="Edm.Decimal" Nullable="false" Precision="5" Scale="0"/>
        <Property Name="Comments" Type="Edm.String" MaxLength="2000" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="Measure" Relationship="State.Or.Leg.API.OData.MeasureCommitteeAgendaItem" ToRole="Measure" FromRole="CommitteeAgendaItem"/>
        <NavigationProperty Name="CommitteeMeeting" Relationship="State.Or.Leg.API.OData.CommitteeMeetingCommitteeAgendaItem" ToRole="CommitteeMeeting" FromRole="CommitteeAgendaItem"/>
        <NavigationProperty Name="CommitteeProposedAmendments" Relationship="State.Or.Leg.API.OData.CommitteeAgendaItemCommitteeProposedAmendment" ToRole="CommitteeProposedAmendment" FromRole="CommitteeAgendaItem"/>
        <NavigationProperty Name="CommitteeVotes" Relationship="State.Or.Leg.API.OData.CommitteeVotesCommitteeAgendaItem" ToRole="CommitteeVotes" FromRole="CommitteeAgendaItem"/>
      </EntityType>
      <EntityType Name="CommitteeStaff">
        <Key>
          <PropertyRef Name="CommitteeStaffId"/>
        </Key>
        <Property Name="CommitteeStaffId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="CommitteeCode" Type="Edm.String" Nullable="false" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="FirstName" Type="Edm.String" MaxLength="30" FixedLength="false" Unicode="false"/>
        <Property Name="LastName" Type="Edm.String" MaxLength="30" FixedLength="false" Unicode="false"/>
        <Property Name="Title" Type="Edm.String" MaxLength="50" FixedLength="false" Unicode="false"/>
        <Property Name="PrintOrder" Type="Edm.Decimal" Nullable="false" Precision="5" Scale="0"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="Committee" Relationship="State.Or.Leg.API.OData.CommitteeCommitteeStaff" ToRole="Committee" FromRole="CommitteeStaff"/>
      </EntityType>
      <EntityType Name="CommitteeMeetingDocument">
        <Key>
          <PropertyRef Name="CommitteeMeetingDocumentId"/>
        </Key>
        <Property Name="CommitteeMeetingDocumentId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="CommitteeCode" Type="Edm.String" Nullable="false" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="MeetingDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ExhibitReference" Type="Edm.String" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="ExhibitTitle" Type="Edm.String" Nullable="false" MaxLength="50" FixedLength="false" Unicode="false"/>
        <Property Name="Submitter" Type="Edm.String" MaxLength="50" FixedLength="false" Unicode="false"/>
        <Property Name="DocumentType" Type="Edm.String" Nullable="false" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="MeasurePrefix" Type="Edm.String" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32"/>
        <Property Name="DocumentUrl" Type="Edm.String" MaxLength="200" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="CommitteeMeeting" Relationship="State.Or.Leg.API.OData.CommitteeMeetingCommitteeMeetingDocument" ToRole="CommitteeMeeting" FromRole="CommitteeMeetingDocument"/>
        <NavigationProperty Name="Measure" Relationship="State.Or.Leg.API.OData.MeasureCommitteeMeetingDocument" ToRole="Measure" FromRole="CommitteeMeetingDocument"/>
      </EntityType>
      <EntityType Name="ConveneTime">
        <Key>
          <PropertyRef Name="Chamber"/>
          <PropertyRef Name="SessionDate"/>
          <PropertyRef Name="SessionKey"/>
        </Key>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="SessionDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="Chamber" Type="Edm.String" Nullable="false" MaxLength="1" FixedLength="false" Unicode="false"/>
        <Property Name="RecessUntil" Type="Edm.DateTime" Precision="3"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="LegislativeSession" Relationship="State.Or.Leg.API.OData.LegislativeSessionConveneTime" ToRole="LegislativeSession" FromRole="ConveneTime"/>
      </EntityType>
      <EntityType Name="FloorSessionAgendaItem">
        <Key>
          <PropertyRef Name="AgendaId"/>
        </Key>
        <Property Name="AgendaId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="MeasurePrefix" Type="Edm.String" Nullable="false" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32" Nullable="false"/>
        <Property Name="ScheduleDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="Version" Type="Edm.String" MaxLength="1" FixedLength="false" Unicode="false"/>
        <Property Name="Chamber" Type="Edm.String" MaxLength="1" FixedLength="false" Unicode="false"/>
        <Property Name="Completed" Type="Edm.Boolean"/>
        <Property Name="OrderOfBusiness" Type="Edm.String" Nullable="false" MaxLength="75" FixedLength="false" Unicode="false"/>
        <Property Name="CarrierCode" Type="Edm.String" MaxLength="50" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="Legislator" Relationship="State.Or.Leg.API.OData.LegislatorFloorSessionAgendaItem" ToRole="Legislator" FromRole="FloorSessionAgendaItem"/>
        <NavigationProperty Name="LegislativeSession" Relationship="State.Or.Leg.API.OData.LegislativeSessionFloorSessionAgendaItem" ToRole="LegislativeSession" FromRole="FloorSessionAgendaItem"/>
        <NavigationProperty Name="Measure" Relationship="State.Or.Leg.API.OData.MeasureFloorSessionAgendaItem" ToRole="Measure" FromRole="FloorSessionAgendaItem"/>
      </EntityType>
      <EntityType Name="Legislator">
        <Key>
          <PropertyRef Name="LegislatorCode"/>
          <PropertyRef Name="SessionKey"/>
        </Key>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="LegislatorCode" Type="Edm.String" Nullable="false" MaxLength="50" FixedLength="false" Unicode="false"/>
        <Property Name="FirstName" Type="Edm.String" Nullable="false" MaxLength="40" FixedLength="false" Unicode="false"/>
        <Property Name="LastName" Type="Edm.String" Nullable="false" MaxLength="50" FixedLength="false" Unicode="false"/>
        <Property Name="CapitolAddress" Type="Edm.String" MaxLength="218" FixedLength="false" Unicode="false"/>
        <Property Name="CapitolPhone" Type="Edm.String" MaxLength="15" FixedLength="false" Unicode="false"/>
        <Property Name="Title" Type="Edm.String" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="Chamber" Type="Edm.String" Nullable="false" MaxLength="1" FixedLength="false" Unicode="false"/>
        <Property Name="Party" Type="Edm.String" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="DistrictNumber" Type="Edm.Decimal" Nullable="false" Precision="4" Scale="0"/>
        <Property Name="EmailAddress" Type="Edm.String" MaxLength="100" FixedLength="false" Unicode="false"/>
        <Property Name="WebSiteUrl" Type="Edm.String" MaxLength="100" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="FloorSessionAgendaItems" Relationship="State.Or.Leg.API.OData.LegislatorFloorSessionAgendaItem" ToRole="FloorSessionAgendaItem" FromRole="Legislator"/>
        <NavigationProperty Name="LegislativeSession" Relationship="State.Or.Leg.API.OData.LegislativeSessionLegislator" ToRole="LegislativeSession" FromRole="Legislator"/>
        <NavigationProperty Name="CommitteeMembers" Relationship="State.Or.Leg.API.OData.LegislatorCommitteeMember" ToRole="CommitteeMember" FromRole="Legislator"/>
      </EntityType>
      <EntityType Name="MeasureAnalysisDocument">
        <Key>
          <PropertyRef Name="MeasureAnalysisId"/>
        </Key>
        <Property Name="MeasureAnalysisId" Type="Edm.Decimal" Nullable="false" Precision="18" Scale="0"/>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="CommittteCode" Type="Edm.String" Nullable="false" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="DocumentType" Type="Edm.String" Nullable="false" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="MeasurePrefix" Type="Edm.String" Nullable="false" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32" Nullable="false"/>
        <Property Name="Version" Type="Edm.String" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="IsMinority" Type="Edm.Boolean"/>
        <Property Name="DocumentUrl" Type="Edm.String" MaxLength="199" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="Measure" Relationship="State.Or.Leg.API.OData.MeasureMeasureAnalysisDocument" ToRole="Measure" FromRole="MeasureAnalysisDocument"/>
        <NavigationProperty Name="Committee" Relationship="State.Or.Leg.API.OData.CommitteeMeasureAnalysisDocument" ToRole="Committee" FromRole="MeasureAnalysisDocument"/>
      </EntityType>
      <EntityType Name="MeasureDocument">
        <Key>
          <PropertyRef Name="MeasureNumber"/>
          <PropertyRef Name="MeasurePrefix"/>
          <PropertyRef Name="SessionKey"/>
          <PropertyRef Name="VersionDescription"/>
        </Key>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="MeasurePrefix" Type="Edm.String" Nullable="false" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32" Nullable="false"/>
        <Property Name="VersionDescription" Type="Edm.String" Nullable="false" MaxLength="200" FixedLength="false" Unicode="false"/>
        <Property Name="DocumentUrl" Type="Edm.String" MaxLength="284" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="Measure" Relationship="State.Or.Leg.API.OData.MeasureMeasureDocument" ToRole="Measure" FromRole="MeasureDocument"/>
      </EntityType>
      <EntityType Name="MeasureHistoryAction">
        <Key>
          <PropertyRef Name="MeasureHistoryId"/>
        </Key>
        <Property Name="MeasureHistoryId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="MeasurePrefix" Type="Edm.String" Nullable="false" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32" Nullable="false"/>
        <Property Name="Chamber" Type="Edm.String" Nullable="false" MaxLength="1" FixedLength="false" Unicode="false"/>
        <Property Name="ActionDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ActionText" Type="Edm.String" MaxLength="1000" FixedLength="false" Unicode="false"/>
        <Property Name="VoteText" Type="Edm.String" MaxLength="3000" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <Property Name="PublicNotification" Type="Edm.Boolean"/>
        <NavigationProperty Name="Measure" Relationship="State.Or.Leg.API.OData.MeasureMeasureHistoryAction" ToRole="Measure" FromRole="MeasureHistoryAction"/>
        <NavigationProperty Name="MeasureVotes" Relationship="State.Or.Leg.API.OData.MeasureHistoryActionMeasureVote" ToRole="MeasureVote" FromRole="MeasureHistoryAction"/>
      </EntityType>
      <EntityType Name="MeasureSponsor">
        <Key>
          <PropertyRef Name="MeasureSponsorId"/>
        </Key>
        <Property Name="MeasureSponsorId" Type="Edm.Decimal" Nullable="false" Precision="18" Scale="0"/>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="MeasurePrefix" Type="Edm.String" Nullable="false" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32" Nullable="false"/>
        <Property Name="SponsorType" Type="Edm.String" Nullable="false" MaxLength="30" FixedLength="false" Unicode="false"/>
        <Property Name="LegislatoreCode" Type="Edm.String" MaxLength="50" FixedLength="false" Unicode="false"/>
        <Property Name="CommitteeCode" Type="Edm.String" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="SponsorLevel" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="PrintOrder" Type="Edm.Decimal" Nullable="false" Precision="18" Scale="0"/>
        <Property Name="PresessionFiledMessage" Type="Edm.String" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="Measure" Relationship="State.Or.Leg.API.OData.MeasureMeasureSponsor" ToRole="Measure" FromRole="MeasureSponsor"/>
        <NavigationProperty Name="Committee" Relationship="State.Or.Leg.API.OData.CommitteeMeasureSponsor" ToRole="Committee" FromRole="MeasureSponsor"/>
      </EntityType>
      <EntityType Name="CommitteeProposedAmendment">
        <Key>
          <PropertyRef Name="ProposedAmendmentId"/>
        </Key>
        <Property Name="ProposedAmendmentId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="CommitteeAgendaItemId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="CommitteeCode" Type="Edm.String" Nullable="false" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="MeetingDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="MeasurePrefix" Type="Edm.String" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32"/>
        <Property Name="AmendmentNumber" Type="Edm.String" Nullable="false" MaxLength="7" FixedLength="false" Unicode="false"/>
        <Property Name="Meaning" Type="Edm.String" Nullable="false" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="ProposedAmendmentUrl" Type="Edm.String" MaxLength="320" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="CommitteeAgendaItem" Relationship="State.Or.Leg.API.OData.CommitteeAgendaItemCommitteeProposedAmendment" ToRole="CommitteeAgendaItem" FromRole="CommitteeProposedAmendment"/>
      </EntityType>
      <EntityType Name="FloorLetter">
        <Key>
          <PropertyRef Name="FloorLetterId"/>
        </Key>
        <Property Name="FloorLetterId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32"/>
        <Property Name="MeasurePrefix" Type="Edm.String" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="LetterDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="Chamber" Type="Edm.String" Nullable="false" MaxLength="1" FixedLength="false" Unicode="false"/>
        <Property Name="LetterDescription" Type="Edm.String" MaxLength="50" FixedLength="false" Unicode="false"/>
        <Property Name="LetterTitle" Type="Edm.String" MaxLength="100" FixedLength="false" Unicode="false"/>
        <Property Name="FloorLetterUrl" Type="Edm.String" MaxLength="314" FixedLength="false" Unicode="false"/>
        <NavigationProperty Name="Measure" Relationship="State.Or.Leg.API.OData.FloorLetterMeasure" ToRole="Measure" FromRole="FloorLetter"/>
        <NavigationProperty Name="LegislativeSession" Relationship="State.Or.Leg.API.OData.LegislativeSessionFloorLetter" ToRole="LegislativeSession" FromRole="FloorLetter"/>
      </EntityType>
      <EntityType Name="CommitteeVote">
        <Key>
          <PropertyRef Name="CommitteeVoteId"/>
        </Key>
        <Property Name="CommitteeVoteId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="CommitteeReportId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="CommitteeAgendaItemId" Type="Edm.Int32"/>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="CommitteeCode" Type="Edm.String" Nullable="false" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="MeetingDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="MeasurePrefix" Type="Edm.String" Nullable="false" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32" Nullable="false"/>
        <Property Name="VoteName" Type="Edm.String" Nullable="false" MaxLength="50" FixedLength="false" Unicode="false"/>
        <Property Name="Meaning" Type="Edm.String" Nullable="false" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="CommitteeAgendaItem" Relationship="State.Or.Leg.API.OData.CommitteeVotesCommitteeAgendaItem" ToRole="CommitteeAgendaItem" FromRole="CommitteeVotes"/>
        <NavigationProperty Name="Measure" Relationship="State.Or.Leg.API.OData.CommitteeVoteMeasure" ToRole="Measure" FromRole="CommitteeVote"/>
      </EntityType>
      <EntityType Name="MeasureVote">
        <Key>
          <PropertyRef Name="MeasureVoteId"/>
        </Key>
        <Property Name="MeasureVoteId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="MeasureHistoryId" Type="Edm.Int32" Nullable="false"/>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="MeasurePrefix" Type="Edm.String" Nullable="false" MaxLength="3" FixedLength="false" Unicode="false"/>
        <Property Name="MeasureNumber" Type="Edm.Int32" Nullable="false"/>
        <Property Name="Vote" Type="Edm.String" Nullable="false" MaxLength="250" FixedLength="false" Unicode="false"/>
        <Property Name="Chamber" Type="Edm.String" Nullable="false" MaxLength="1" FixedLength="false" Unicode="false"/>
        <Property Name="ActionDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ActionText" Type="Edm.String" MaxLength="1000" FixedLength="false" Unicode="false"/>
        <Property Name="VoteName" Type="Edm.String" Nullable="false" MaxLength="50" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="Measure" Relationship="State.Or.Leg.API.OData.MeasureMeasureVote" ToRole="Measure" FromRole="MeasureVote"/>
        <NavigationProperty xmlns:p6="http://schemas.microsoft.com/ado/2006/04/codegeneration" Name="MeasureHistoryAction" Relationship="State.Or.Leg.API.OData.MeasureHistoryActionMeasureVote" ToRole="MeasureHistoryAction" FromRole="MeasureVote" p6:GetterAccess="Public" p6:SetterAccess="Public"/>
      </EntityType>
      <EntityType Name="CommitteeMember">
        <Key>
          <PropertyRef Name="CommitteeCode"/>
          <PropertyRef Name="CreatedDate"/>
          <PropertyRef Name="Title"/>
        </Key>
        <Property Name="SessionKey" Type="Edm.String" Nullable="false" MaxLength="10" FixedLength="false" Unicode="false"/>
        <Property Name="CommitteeCode" Type="Edm.String" Nullable="false" MaxLength="6" FixedLength="false" Unicode="false"/>
        <Property Name="LegislatorCode" Type="Edm.String" MaxLength="54" FixedLength="false" Unicode="false"/>
        <Property Name="Title" Type="Edm.String" Nullable="false" MaxLength="20" FixedLength="false" Unicode="false"/>
        <Property Name="CreatedDate" Type="Edm.DateTime" Nullable="false" Precision="3"/>
        <Property Name="ModifiedDate" Type="Edm.DateTime" Precision="3"/>
        <NavigationProperty Name="LegislativeSession" Relationship="State.Or.Leg.API.OData.LegislativeSessionCommitteeMember" ToRole="LegislativeSession" FromRole="CommitteeMember"/>
        <NavigationProperty Name="Committee" Relationship="State.Or.Leg.API.OData.CommitteeCommitteeMember" ToRole="Committee" FromRole="CommitteeMember"/>
        <NavigationProperty Name="Legislator" Relationship="State.Or.Leg.API.OData.LegislatorCommitteeMember" ToRole="Legislator" FromRole="CommitteeMember"/>
      </EntityType>
      <Association Name="LegislativeSessionMeasure">
        <End Type="State.Or.Leg.API.OData.LegislativeSession" Role="LegislativeSession" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.Measure" Role="Measure" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="LegislativeSession">
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="Measure">
            <PropertyRef Name="SessionKey"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="LegislativeSessionCommittees">
        <End Type="State.Or.Leg.API.OData.LegislativeSession" Role="LegislativeSession" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.Committee" Role="Committees" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="LegislativeSession">
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="Committees">
            <PropertyRef Name="SessionKey"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="LegislativeSessionLegislator">
        <End Type="State.Or.Leg.API.OData.LegislativeSession" Role="LegislativeSession" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.Legislator" Role="Legislator" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="LegislativeSession">
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="Legislator">
            <PropertyRef Name="SessionKey"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="LegislativeSessionConveneTime">
        <End Type="State.Or.Leg.API.OData.LegislativeSession" Role="LegislativeSession" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.ConveneTime" Role="ConveneTime" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="LegislativeSession">
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="ConveneTime">
            <PropertyRef Name="SessionKey"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="LegislativeSessionFloorSessionAgendaItem">
        <End Type="State.Or.Leg.API.OData.LegislativeSession" Role="LegislativeSession" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.FloorSessionAgendaItem" Role="FloorSessionAgendaItem" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="LegislativeSession">
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="FloorSessionAgendaItem">
            <PropertyRef Name="SessionKey"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="LegislativeSessionFloorLetter">
        <End Type="State.Or.Leg.API.OData.LegislativeSession" Role="LegislativeSession" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.FloorLetter" Role="FloorLetter" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="LegislativeSession">
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="FloorLetter">
            <PropertyRef Name="SessionKey"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="LegislativeSessionCommitteeMember">
        <End Type="State.Or.Leg.API.OData.LegislativeSession" Role="LegislativeSession" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeMember" Role="CommitteeMember" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="LegislativeSession">
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="CommitteeMember">
            <PropertyRef Name="SessionKey"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="MeasureCommitteeAgendaItem">
        <End Type="State.Or.Leg.API.OData.Measure" Role="Measure" Multiplicity="0..1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeAgendaItem" Role="CommitteeAgendaItem" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Measure">
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="CommitteeAgendaItem">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="MeasureCommitteeMeetingDocument">
        <End Type="State.Or.Leg.API.OData.Measure" Role="Measure" Multiplicity="0..1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeMeetingDocument" Role="CommitteeMeetingDocument" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Measure">
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="CommitteeMeetingDocument">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="MeasureFloorSessionAgendaItem">
        <End Type="State.Or.Leg.API.OData.Measure" Role="Measure" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.FloorSessionAgendaItem" Role="FloorSessionAgendaItem" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Measure">
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="FloorSessionAgendaItem">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="MeasureMeasureDocument">
        <End Type="State.Or.Leg.API.OData.Measure" Role="Measure" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.MeasureDocument" Role="MeasureDocument" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Measure">
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="MeasureDocument">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="MeasureMeasureAnalysisDocument">
        <End Type="State.Or.Leg.API.OData.Measure" Role="Measure" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.MeasureAnalysisDocument" Role="MeasureAnalysisDocument" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Measure">
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="MeasureAnalysisDocument">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="MeasureMeasureHistoryAction">
        <End Type="State.Or.Leg.API.OData.Measure" Role="Measure" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.MeasureHistoryAction" Role="MeasureHistoryAction" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Measure">
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="MeasureHistoryAction">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="MeasureMeasureSponsor">
        <End Type="State.Or.Leg.API.OData.Measure" Role="Measure" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.MeasureSponsor" Role="MeasureSponsor" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Measure">
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="MeasureSponsor">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="FloorLetterMeasure">
        <End Type="State.Or.Leg.API.OData.Measure" Role="Measure" Multiplicity="0..1"/>
        <End Type="State.Or.Leg.API.OData.FloorLetter" Role="FloorLetter" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Measure">
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="FloorLetter">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="MeasureMeasureVote">
        <End Type="State.Or.Leg.API.OData.Measure" Role="Measure" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.MeasureVote" Role="MeasureVote" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Measure">
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="MeasureVote">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="CommitteeVoteMeasure">
        <End Type="State.Or.Leg.API.OData.Measure" Role="Measure" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeVote" Role="CommitteeVote" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Measure">
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="CommitteeVote">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeasureNumber"/>
            <PropertyRef Name="MeasurePrefix"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="CommitteesCommitteeMeetings">
        <End Type="State.Or.Leg.API.OData.Committee" Role="Committees" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeMeeting" Role="CommitteeMeetings" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Committees">
            <PropertyRef Name="CommitteeCode"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="CommitteeMeetings">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="CommitteeCode"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="CommitteesParentCommittees">
        <End Type="State.Or.Leg.API.OData.Committee" Role="Committees1" Multiplicity="0..1"/>
        <End Type="State.Or.Leg.API.OData.Committee" Role="Committees" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Committees1">
            <PropertyRef Name="CommitteeCode"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="Committees">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="ParentCommitteeCode"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="CommitteeCommitteeStaff">
        <End Type="State.Or.Leg.API.OData.Committee" Role="Committee" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeStaff" Role="CommitteeStaff" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Committee">
            <PropertyRef Name="CommitteeCode"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="CommitteeStaff">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="CommitteeCode"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="CommitteeMeasureAnalysisDocument">
        <End Type="State.Or.Leg.API.OData.Committee" Role="Committee" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.MeasureAnalysisDocument" Role="MeasureAnalysisDocument" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Committee">
            <PropertyRef Name="CommitteeCode"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="MeasureAnalysisDocument">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="CommittteCode"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="CommitteeMeasureSponsor">
        <End Type="State.Or.Leg.API.OData.Committee" Role="Committee" Multiplicity="0..1"/>
        <End Type="State.Or.Leg.API.OData.MeasureSponsor" Role="MeasureSponsor" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Committee">
            <PropertyRef Name="CommitteeCode"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="MeasureSponsor">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="CommitteeCode"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="CommitteeCommitteeMember">
        <End Type="State.Or.Leg.API.OData.Committee" Role="Committee" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeMember" Role="CommitteeMember" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Committee">
            <PropertyRef Name="CommitteeCode"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="CommitteeMember">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="CommitteeCode"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="CommitteeMeetingCommitteeAgendaItem">
        <End Type="State.Or.Leg.API.OData.CommitteeMeeting" Role="CommitteeMeeting" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeAgendaItem" Role="CommitteeAgendaItem" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="CommitteeMeeting">
            <PropertyRef Name="CommitteeCode"/>
            <PropertyRef Name="MeetingDate"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="CommitteeAgendaItem">
            <PropertyRef Name="CommitteCode"/>
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeetingDate"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="CommitteeMeetingCommitteeMeetingDocument">
        <End Type="State.Or.Leg.API.OData.CommitteeMeeting" Role="CommitteeMeeting" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeMeetingDocument" Role="CommitteeMeetingDocument" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="CommitteeMeeting">
            <PropertyRef Name="CommitteeCode"/>
            <PropertyRef Name="MeetingDate"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="CommitteeMeetingDocument">
            <PropertyRef Name="CommitteeCode"/>
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="MeetingDate"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="CommitteeAgendaItemCommitteeProposedAmendment">
        <End Type="State.Or.Leg.API.OData.CommitteeAgendaItem" Role="CommitteeAgendaItem" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeProposedAmendment" Role="CommitteeProposedAmendment" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="CommitteeAgendaItem">
            <PropertyRef Name="CommitteeAgendaItemId"/>
          </Principal>
          <Dependent Role="CommitteeProposedAmendment">
            <PropertyRef Name="CommitteeAgendaItemId"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="CommitteeVotesCommitteeAgendaItem">
        <End Type="State.Or.Leg.API.OData.CommitteeAgendaItem" Role="CommitteeAgendaItem" Multiplicity="0..1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeVote" Role="CommitteeVotes" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="CommitteeAgendaItem">
            <PropertyRef Name="CommitteeAgendaItemId"/>
          </Principal>
          <Dependent Role="CommitteeVotes">
            <PropertyRef Name="CommitteeAgendaItemId"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="LegislatorFloorSessionAgendaItem">
        <End Type="State.Or.Leg.API.OData.Legislator" Role="Legislator" Multiplicity="0..1"/>
        <End Type="State.Or.Leg.API.OData.FloorSessionAgendaItem" Role="FloorSessionAgendaItem" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Legislator">
            <PropertyRef Name="LegislatorCode"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="FloorSessionAgendaItem">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="CarrierCode"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="LegislatorCommitteeMember">
        <End Type="State.Or.Leg.API.OData.Legislator" Role="Legislator" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.CommitteeMember" Role="CommitteeMember" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="Legislator">
            <PropertyRef Name="LegislatorCode"/>
            <PropertyRef Name="SessionKey"/>
          </Principal>
          <Dependent Role="CommitteeMember">
            <PropertyRef Name="SessionKey"/>
            <PropertyRef Name="LegislatorCode"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
      <Association Name="MeasureHistoryActionMeasureVote">
        <End Type="State.Or.Leg.API.OData.MeasureHistoryAction" Role="MeasureHistoryAction" Multiplicity="1"/>
        <End Type="State.Or.Leg.API.OData.MeasureVote" Role="MeasureVote" Multiplicity="*"/>
        <ReferentialConstraint>
          <Principal Role="MeasureHistoryAction">
            <PropertyRef Name="MeasureHistoryId"/>
          </Principal>
          <Dependent Role="MeasureVote">
            <PropertyRef Name="MeasureHistoryId"/>
          </Dependent>
        </ReferentialConstraint>
      </Association>
    </Schema>
    <Schema xmlns="http://schemas.microsoft.com/ado/2009/11/edm" Namespace="State.Or.Leg.API.Entites">
      <EntityContainer Name="ApiEntities" m:IsDefaultEntityContainer="true">
        <EntitySet Name="LegislativeSessions" EntityType="State.Or.Leg.API.OData.LegislativeSession"/>
        <EntitySet Name="Measures" EntityType="State.Or.Leg.API.OData.Measure"/>
        <EntitySet Name="Committees" EntityType="State.Or.Leg.API.OData.Committee"/>
        <EntitySet Name="CommitteeMeetings" EntityType="State.Or.Leg.API.OData.CommitteeMeeting"/>
        <EntitySet Name="CommitteeAgendaItems" EntityType="State.Or.Leg.API.OData.CommitteeAgendaItem"/>
        <EntitySet Name="CommitteeStaffMembers" EntityType="State.Or.Leg.API.OData.CommitteeStaff"/>
        <EntitySet Name="CommitteeMeetingDocuments" EntityType="State.Or.Leg.API.OData.CommitteeMeetingDocument"/>
        <EntitySet Name="ConveneTimes" EntityType="State.Or.Leg.API.OData.ConveneTime"/>
        <EntitySet Name="FloorSessionAgendaItems" EntityType="State.Or.Leg.API.OData.FloorSessionAgendaItem"/>
        <EntitySet Name="Legislators" EntityType="State.Or.Leg.API.OData.Legislator"/>
        <EntitySet Name="MeasureAnalysisDocuments" EntityType="State.Or.Leg.API.OData.MeasureAnalysisDocument"/>
        <EntitySet Name="MeasureDocuments" EntityType="State.Or.Leg.API.OData.MeasureDocument"/>
        <EntitySet Name="MeasureHistoryActions" EntityType="State.Or.Leg.API.OData.MeasureHistoryAction"/>
        <EntitySet Name="MeasureSponsors" EntityType="State.Or.Leg.API.OData.MeasureSponsor"/>
        <EntitySet Name="CommitteeProposedAmendments" EntityType="State.Or.Leg.API.OData.CommitteeProposedAmendment"/>
        <EntitySet Name="FloorLetters" EntityType="State.Or.Leg.API.OData.FloorLetter"/>
        <EntitySet Name="CommitteeVotes" EntityType="State.Or.Leg.API.OData.CommitteeVote"/>
        <EntitySet Name="MeasureVotes" EntityType="State.Or.Leg.API.OData.MeasureVote"/>
        <EntitySet Name="CommitteeMembers" EntityType="State.Or.Leg.API.OData.CommitteeMember"/>
        <AssociationSet Name="LegislativeSessionMeasure" Association="State.Or.Leg.API.OData.LegislativeSessionMeasure">
          <End Role="LegislativeSession" EntitySet="LegislativeSessions"/>
          <End Role="Measure" EntitySet="Measures"/>
        </AssociationSet>
        <AssociationSet Name="LegislativeSessionCommittees" Association="State.Or.Leg.API.OData.LegislativeSessionCommittees">
          <End Role="LegislativeSession" EntitySet="LegislativeSessions"/>
          <End Role="Committees" EntitySet="Committees"/>
        </AssociationSet>
        <AssociationSet Name="LegislativeSessionLegislator" Association="State.Or.Leg.API.OData.LegislativeSessionLegislator">
          <End Role="LegislativeSession" EntitySet="LegislativeSessions"/>
          <End Role="Legislator" EntitySet="Legislators"/>
        </AssociationSet>
        <AssociationSet Name="LegislativeSessionConveneTime" Association="State.Or.Leg.API.OData.LegislativeSessionConveneTime">
          <End Role="LegislativeSession" EntitySet="LegislativeSessions"/>
          <End Role="ConveneTime" EntitySet="ConveneTimes"/>
        </AssociationSet>
        <AssociationSet Name="LegislativeSessionFloorSessionAgendaItem" Association="State.Or.Leg.API.OData.LegislativeSessionFloorSessionAgendaItem">
          <End Role="LegislativeSession" EntitySet="LegislativeSessions"/>
          <End Role="FloorSessionAgendaItem" EntitySet="FloorSessionAgendaItems"/>
        </AssociationSet>
        <AssociationSet Name="LegislativeSessionFloorLetter" Association="State.Or.Leg.API.OData.LegislativeSessionFloorLetter">
          <End Role="LegislativeSession" EntitySet="LegislativeSessions"/>
          <End Role="FloorLetter" EntitySet="FloorLetters"/>
        </AssociationSet>
        <AssociationSet Name="LegislativeSessionCommitteeMember" Association="State.Or.Leg.API.OData.LegislativeSessionCommitteeMember">
          <End Role="LegislativeSession" EntitySet="LegislativeSessions"/>
          <End Role="CommitteeMember" EntitySet="CommitteeMembers"/>
        </AssociationSet>
        <AssociationSet Name="MeasureCommitteeAgendaItem" Association="State.Or.Leg.API.OData.MeasureCommitteeAgendaItem">
          <End Role="Measure" EntitySet="Measures"/>
          <End Role="CommitteeAgendaItem" EntitySet="CommitteeAgendaItems"/>
        </AssociationSet>
        <AssociationSet Name="MeasureCommitteeMeetingDocument" Association="State.Or.Leg.API.OData.MeasureCommitteeMeetingDocument">
          <End Role="Measure" EntitySet="Measures"/>
          <End Role="CommitteeMeetingDocument" EntitySet="CommitteeMeetingDocuments"/>
        </AssociationSet>
        <AssociationSet Name="MeasureFloorSessionAgendaItem" Association="State.Or.Leg.API.OData.MeasureFloorSessionAgendaItem">
          <End Role="Measure" EntitySet="Measures"/>
          <End Role="FloorSessionAgendaItem" EntitySet="FloorSessionAgendaItems"/>
        </AssociationSet>
        <AssociationSet Name="MeasureMeasureDocument" Association="State.Or.Leg.API.OData.MeasureMeasureDocument">
          <End Role="Measure" EntitySet="Measures"/>
          <End Role="MeasureDocument" EntitySet="MeasureDocuments"/>
        </AssociationSet>
        <AssociationSet Name="MeasureMeasureAnalysisDocument" Association="State.Or.Leg.API.OData.MeasureMeasureAnalysisDocument">
          <End Role="Measure" EntitySet="Measures"/>
          <End Role="MeasureAnalysisDocument" EntitySet="MeasureAnalysisDocuments"/>
        </AssociationSet>
        <AssociationSet Name="MeasureMeasureHistoryAction" Association="State.Or.Leg.API.OData.MeasureMeasureHistoryAction">
          <End Role="Measure" EntitySet="Measures"/>
          <End Role="MeasureHistoryAction" EntitySet="MeasureHistoryActions"/>
        </AssociationSet>
        <AssociationSet Name="MeasureMeasureSponsor" Association="State.Or.Leg.API.OData.MeasureMeasureSponsor">
          <End Role="Measure" EntitySet="Measures"/>
          <End Role="MeasureSponsor" EntitySet="MeasureSponsors"/>
        </AssociationSet>
        <AssociationSet Name="FloorLetterMeasure" Association="State.Or.Leg.API.OData.FloorLetterMeasure">
          <End Role="Measure" EntitySet="Measures"/>
          <End Role="FloorLetter" EntitySet="FloorLetters"/>
        </AssociationSet>
        <AssociationSet Name="MeasureMeasureVote" Association="State.Or.Leg.API.OData.MeasureMeasureVote">
          <End Role="Measure" EntitySet="Measures"/>
          <End Role="MeasureVote" EntitySet="MeasureVotes"/>
        </AssociationSet>
        <AssociationSet Name="CommitteeVoteMeasure" Association="State.Or.Leg.API.OData.CommitteeVoteMeasure">
          <End Role="Measure" EntitySet="Measures"/>
          <End Role="CommitteeVote" EntitySet="CommitteeVotes"/>
        </AssociationSet>
        <AssociationSet Name="CommitteesCommitteeMeetings" Association="State.Or.Leg.API.OData.CommitteesCommitteeMeetings">
          <End Role="Committees" EntitySet="Committees"/>
          <End Role="CommitteeMeetings" EntitySet="CommitteeMeetings"/>
        </AssociationSet>
        <AssociationSet Name="CommitteesParentCommittees" Association="State.Or.Leg.API.OData.CommitteesParentCommittees">
          <End Role="Committees" EntitySet="Committees"/>
          <End Role="Committees1" EntitySet="Committees"/>
        </AssociationSet>
        <AssociationSet Name="CommitteeCommitteeStaff" Association="State.Or.Leg.API.OData.CommitteeCommitteeStaff">
          <End Role="Committee" EntitySet="Committees"/>
          <End Role="CommitteeStaff" EntitySet="CommitteeStaffMembers"/>
        </AssociationSet>
        <AssociationSet Name="CommitteeMeasureAnalysisDocument" Association="State.Or.Leg.API.OData.CommitteeMeasureAnalysisDocument">
          <End Role="Committee" EntitySet="Committees"/>
          <End Role="MeasureAnalysisDocument" EntitySet="MeasureAnalysisDocuments"/>
        </AssociationSet>
        <AssociationSet Name="CommitteeMeasureSponsor" Association="State.Or.Leg.API.OData.CommitteeMeasureSponsor">
          <End Role="Committee" EntitySet="Committees"/>
          <End Role="MeasureSponsor" EntitySet="MeasureSponsors"/>
        </AssociationSet>
        <AssociationSet Name="CommitteeCommitteeMember" Association="State.Or.Leg.API.OData.CommitteeCommitteeMember">
          <End Role="Committee" EntitySet="Committees"/>
          <End Role="CommitteeMember" EntitySet="CommitteeMembers"/>
        </AssociationSet>
        <AssociationSet Name="CommitteeMeetingCommitteeAgendaItem" Association="State.Or.Leg.API.OData.CommitteeMeetingCommitteeAgendaItem">
          <End Role="CommitteeMeeting" EntitySet="CommitteeMeetings"/>
          <End Role="CommitteeAgendaItem" EntitySet="CommitteeAgendaItems"/>
        </AssociationSet>
        <AssociationSet Name="CommitteeMeetingCommitteeMeetingDocument" Association="State.Or.Leg.API.OData.CommitteeMeetingCommitteeMeetingDocument">
          <End Role="CommitteeMeeting" EntitySet="CommitteeMeetings"/>
          <End Role="CommitteeMeetingDocument" EntitySet="CommitteeMeetingDocuments"/>
        </AssociationSet>
        <AssociationSet Name="CommitteeAgendaItemCommitteeProposedAmendment" Association="State.Or.Leg.API.OData.CommitteeAgendaItemCommitteeProposedAmendment">
          <End Role="CommitteeAgendaItem" EntitySet="CommitteeAgendaItems"/>
          <End Role="CommitteeProposedAmendment" EntitySet="CommitteeProposedAmendments"/>
        </AssociationSet>
        <AssociationSet Name="CommitteeVotesCommitteeAgendaItem" Association="State.Or.Leg.API.OData.CommitteeVotesCommitteeAgendaItem">
          <End Role="CommitteeAgendaItem" EntitySet="CommitteeAgendaItems"/>
          <End Role="CommitteeVotes" EntitySet="CommitteeVotes"/>
        </AssociationSet>
        <AssociationSet Name="LegislatorFloorSessionAgendaItem" Association="State.Or.Leg.API.OData.LegislatorFloorSessionAgendaItem">
          <End Role="FloorSessionAgendaItem" EntitySet="FloorSessionAgendaItems"/>
          <End Role="Legislator" EntitySet="Legislators"/>
        </AssociationSet>
        <AssociationSet Name="LegislatorCommitteeMember" Association="State.Or.Leg.API.OData.LegislatorCommitteeMember">
          <End Role="Legislator" EntitySet="Legislators"/>
          <End Role="CommitteeMember" EntitySet="CommitteeMembers"/>
        </AssociationSet>
        <AssociationSet Name="MeasureHistoryActionMeasureVote" Association="State.Or.Leg.API.OData.MeasureHistoryActionMeasureVote">
          <End Role="MeasureHistoryAction" EntitySet="MeasureHistoryActions"/>
          <End Role="MeasureVote" EntitySet="MeasureVotes"/>
        </AssociationSet>
      </EntityContainer>
    </Schema>
  </edmx:DataServices>
</edmx:Edmx>"""
