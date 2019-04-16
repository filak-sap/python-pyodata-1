from pyodata.v2.model import schema_from_xml

def test_parse_metadata(metadata_api_oregonlegislature_gov):
    schema = schema_from_xml(metadata_api_oregonlegislature_gov)
    assert [es.name for es in schema.entity_sets] == ['LegislativeSessions',
                                                        'Measures',
                                                        'Committees',
                                                        'CommitteeMeetings',
                                                        'CommitteeAgendaItems',
                                                        'CommitteeStaffMembers',
                                                        'CommitteeMeetingDocuments',
                                                        'ConveneTimes',
                                                        'FloorSessionAgendaItems',
                                                        'Legislators',
                                                        'MeasureAnalysisDocuments',
                                                        'MeasureDocuments',
                                                        'MeasureHistoryActions',
                                                        'MeasureSponsors',
                                                        'CommitteeProposedAmendments',
                                                        'FloorLetters',
                                                        'CommitteeVotes',
                                                        'MeasureVotes',
                                                        'CommitteeMembers']
